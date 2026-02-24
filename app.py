import json
import os
import secrets
import shutil
from datetime import timedelta
from functools import wraps
from pathlib import Path

try:
    import cv2
except ModuleNotFoundError:
    cv2 = None

from flask import Flask, abort, flash, redirect, render_template, request, send_file, session, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

# ---------------- APP CONFIG ----------------

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", secrets.token_hex(32))
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    REMEMBER_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME=timedelta(hours=10),
    MAX_CONTENT_LENGTH=1024 * 1024 * 1024,  # 1GB
)

# ---------------- PATH CONFIG ----------------

BASE_DIR = Path(r"E:\server--\vedio-local")

VIDEO_PATH = BASE_DIR / "assets" / "vedios"
IMAGE_PATH = BASE_DIR / "assets" / "image"
THUMB_PATH = BASE_DIR / "assets" / "thubnail"
ALT_THUMB_PATH = BASE_DIR / "assets" / "thumbnail"   # alt spelling support
PENDING_PATH = BASE_DIR / "assets" / "not-approve-vedio"

LOGIN_PASS_FILE = BASE_DIR / "all-pass" / "login-pass.json"
ADMIN_PASS_FILE = BASE_DIR / "all-pass" / "adminpass.json"

VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".webm"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
MEDIA_EXTENSIONS = VIDEO_EXTENSIONS | IMAGE_EXTENSIONS

# ---------------- AUTO CREATE DIRS ----------------

for p in [
    VIDEO_PATH,
    IMAGE_PATH,
    THUMB_PATH,
    ALT_THUMB_PATH,
    PENDING_PATH,
    LOGIN_PASS_FILE.parent
]:
    p.mkdir(parents=True, exist_ok=True)

# ---------------- AUTH HELPERS ----------------

def _read_json_file(file_path: Path, default):
    if not file_path.exists() or file_path.stat().st_size == 0:
        return default
    try:
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return default


def _verify_password(saved_password: str, entered_password: str) -> bool:
    if not saved_password:
        return False
    if saved_password.startswith(("pbkdf2:", "scrypt:")):
        return check_password_hash(saved_password, entered_password)
    return secrets.compare_digest(saved_password, entered_password)


def load_login_users():
    raw = _read_json_file(LOGIN_PASS_FILE, default={})
    users = {}

    if isinstance(raw, dict) and "users" in raw:
        entries = raw["users"]
    elif isinstance(raw, list):
        entries = raw
    elif isinstance(raw, dict) and "username" in raw:
        entries = [raw]
    else:
        entries = []

    for item in entries:
        if not isinstance(item, dict):
            continue
        username = str(item.get("username", "")).strip()
        password = str(item.get("password", ""))
        role = str(item.get("role", "user")).lower()
        if username and password:
            users[username] = {
                "password": password,
                "role": "admin" if role == "admin" else "user"
            }
    return users


def load_admin_secret():
    raw = _read_json_file(ADMIN_PASS_FILE, default={})
    if isinstance(raw, dict):
        return str(raw.get("password") or raw.get("admin_password") or "")
    if isinstance(raw, str):
        return raw
    return ""


# ---------------- LOGIN SYSTEM ----------------

class User(UserMixin):
    def __init__(self, user_id: str, role: str = "user"):
        self.id = user_id
        self.role = role


login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id: str):
    users = load_login_users()
    if user_id in users:
        return User(user_id, role=users[user_id]["role"])
    return None


def admin_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            return login_manager.unauthorized()
        if not session.get("is_admin"):
            flash("Admin access required.")
            return redirect(url_for("admin_login"))
        return view_func(*args, **kwargs)
    return wrapped


# ---------------- SECURITY ----------------

def safe_media_path(base_path: Path, filename: str) -> Path:
    clean_name = secure_filename(filename)
    candidate = (base_path / clean_name).resolve()
    base_resolved = base_path.resolve()

    if base_resolved not in candidate.parents and candidate != base_resolved:
        abort(400)
    return candidate


def allowed_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in MEDIA_EXTENSIONS


def media_kind(filename: str) -> str:
    return "video" if Path(filename).suffix.lower() in VIDEO_EXTENSIONS else "image"


# ---------------- OPENCV THUMBNAIL ENGINE ----------------

def generate_thumbnail_opencv(video_filename):
    if cv2 is None:
        return False

    video_file_path = str(VIDEO_PATH / video_filename)
    thumb_file_path = str(THUMB_PATH / f"{Path(video_filename).stem}.jpg")

    if os.path.exists(thumb_file_path):
        return True

    cap = cv2.VideoCapture(video_file_path)
    if not cap.isOpened():
        return False

    cap.set(cv2.CAP_PROP_POS_MSEC, 2000)
    success, frame = cap.read()

    if success:
        h, w = frame.shape[:2]
        resized = cv2.resize(frame, (400, int(h * (400 / w))))
        cv2.imwrite(thumb_file_path, resized)

    cap.release()
    return success


# ---------------- ROUTES ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        users = load_login_users()
        user_data = users.get(username)

        if user_data and _verify_password(user_data["password"], password):
            login_user(User(username, role=user_data["role"]))
            session["is_admin"] = user_data["role"] == "admin"
            session.permanent = True
            return redirect(url_for("home"))

        flash("Wrong username or password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/admin/login", methods=["GET", "POST"])
@login_required
def admin_login():
    if request.method == "POST":
        entered_pass = request.form.get("admin_password", "")
        configured_pass = load_admin_secret()

        if configured_pass and _verify_password(configured_pass, entered_pass):
            session["is_admin"] = True
            flash("Admin mode enabled.")
            return redirect(url_for("admin_panel"))

        flash("Invalid admin password.")
        return redirect(url_for("admin_login"))

    return render_template("admin_login.html")


@app.route("/")
@app.route("/home")
@login_required
def home():
    videos = []
    if VIDEO_PATH.exists():
        for f in os.listdir(VIDEO_PATH):
            if f.lower().endswith(tuple(VIDEO_EXTENSIONS)):
                generate_thumbnail_opencv(f)
                videos.append({
                    "name": f,
                    "title": Path(f).stem.replace("_", " ").title(),
                    "thumb": f"{Path(f).stem}.jpg",
                })
    return render_template("home.html", videos=videos)


@app.route("/gallery")
@login_required
def gallery():
    images = []
    if IMAGE_PATH.exists():
        for f in os.listdir(IMAGE_PATH):
            if f.lower().endswith(tuple(IMAGE_EXTENSIONS)):
                images.append({
                    "name": f,
                    "title": Path(f).stem.replace("_", " ").title()
                })
    return render_template("gallery.html", images=images)


@app.route("/creator/free", methods=["GET", "POST"])
@login_required
def free_creator():
    return creator_upload("free")


@app.route("/creator/paid", methods=["GET", "POST"])
@login_required
def paid_creator():
    return creator_upload("paid")


def creator_upload(plan_name: str):
    if request.method == "POST":
        file = request.files.get("media_file")
        if not file or not file.filename:
            flash("Please choose a file.")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("File type not allowed.")
            return redirect(request.url)

        safe_name = secure_filename(file.filename)
        destination = safe_media_path(PENDING_PATH, safe_name)

        if destination.exists():
            flash("File already exists in pending.")
            return redirect(request.url)

        file.save(destination)
        flash(f"Upload successful ({plan_name} creator). Awaiting admin approval.")
        return redirect(request.url)

    return render_template("creator_upload.html", plan_name=plan_name)


@app.route("/admin")
@login_required
@admin_required
def admin_panel():
    pending_files = sorted([p.name for p in PENDING_PATH.iterdir() if p.is_file()])
    approved_files = (
        sorted([p.name for p in VIDEO_PATH.iterdir() if p.is_file()]) +
        sorted([p.name for p in IMAGE_PATH.iterdir() if p.is_file()])
    )
    return render_template("admin.html", pending_files=pending_files, approved_files=approved_files)


@app.post("/admin/approve")
@login_required
@admin_required
def approve_media():
    filename = request.form.get("filename", "")
    source = safe_media_path(PENDING_PATH, filename)

    if not source.exists():
        abort(404)

    destination_base = VIDEO_PATH if media_kind(source.name) == "video" else IMAGE_PATH
    destination = safe_media_path(destination_base, source.name)

    shutil.move(str(source), str(destination))
    flash("Media approved.")
    return redirect(url_for("admin_panel"))


@app.post("/admin/delete")
@login_required
@admin_required
def delete_media():
    filename = request.form.get("filename", "")
    location = request.form.get("location", "pending")

    if location == "pending":
        target = safe_media_path(PENDING_PATH, filename)
    else:
        video_target = safe_media_path(VIDEO_PATH, filename)
        image_target = safe_media_path(IMAGE_PATH, filename)
        target = video_target if video_target.exists() else image_target

    if not target.exists():
        abort(404)

    target.unlink()
    flash("File deleted.")
    return redirect(url_for("admin_panel"))


@app.post("/admin/rename")
@login_required
@admin_required
def rename_media():
    filename = request.form.get("filename", "")
    new_name = request.form.get("new_name", "")
    location = request.form.get("location", "pending")

    if not new_name or not allowed_file(new_name):
        flash("Invalid new name.")
        return redirect(url_for("admin_panel"))

    if location == "pending":
        base = PENDING_PATH
    else:
        base = VIDEO_PATH if safe_media_path(VIDEO_PATH, filename).exists() else IMAGE_PATH

    source = safe_media_path(base, filename)
    destination = safe_media_path(base, new_name)

    if destination.exists():
        flash("File already exists.")
        return redirect(url_for("admin_panel"))

    source.rename(destination)
    flash("File renamed.")
    return redirect(url_for("admin_panel"))


@app.route("/video/<path:filename>")
@login_required
def stream_video(filename):
    file_path = safe_media_path(VIDEO_PATH, filename)
    if not file_path.exists():
        abort(404)
    return send_file(file_path, conditional=True)


@app.route("/serve_image/<path:filename>")
@login_required
def serve_image(filename):
    approved_image = safe_media_path(IMAGE_PATH, filename)
    if approved_image.exists():
        return send_file(approved_image)

    pending_image = safe_media_path(PENDING_PATH, filename)
    if pending_image.exists() and session.get("is_admin"):
        return send_file(pending_image)

    abort(404)


@app.route("/serve_thumb/<path:filename>")
@login_required
def serve_thumb(filename):
    path = safe_media_path(THUMB_PATH, filename)
    alt_path = safe_media_path(ALT_THUMB_PATH, filename)

    if path.exists():
        return send_file(path)
    if alt_path.exists():
        return send_file(alt_path)

    default_img = IMAGE_PATH / "default.jpg"
    if default_img.exists():
        return send_file(default_img)
    abort(404)


@app.route("/logout")
def logout():
    session.pop("is_admin", None)
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)