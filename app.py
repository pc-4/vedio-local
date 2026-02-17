import os
import cv2
from pathlib import Path
from flask import Flask, render_template, redirect, url_for, request, send_file, flash, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'lado-secure-key'

# --- CONFIGURATION ---
BASE_DIR = Path(r'E:\server--\vedio-local')
VIDEO_PATH = BASE_DIR / 'assets' / 'vedios'
IMAGE_PATH = BASE_DIR / 'assets' / 'image'
THUMB_PATH = BASE_DIR / 'assets' / 'thubnail'

# Create all folders if they don't exist
for p in [VIDEO_PATH, IMAGE_PATH, THUMB_PATH]:
    p.mkdir(parents=True, exist_ok=True)

# --- LOGIN SETUP ---
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.role = "admin" if id == "lado" else "user"

@login_manager.user_loader
def load_user(id):
    return User(id)

# --- OPENCV THUMBNAIL ENGINE ---
def generate_thumbnail_opencv(video_filename):
    video_file_path = str(VIDEO_PATH / video_filename)
    thumb_file_path = str(THUMB_PATH / f"{Path(video_filename).stem}.jpg")

    if os.path.exists(thumb_file_path):
        return True

    cap = cv2.VideoCapture(video_file_path)
    if not cap.isOpened():
        return False

    # Jump to 2 seconds (2000ms) to avoid black start frames
    cap.set(cv2.CAP_PROP_POS_MSEC, 2000)
    success, frame = cap.read()
    if success:
        # Resize for performance
        height, width = frame.shape[:2]
        resized = cv2.resize(frame, (400, int(height * (400 / width))))
        cv2.imwrite(thumb_file_path, resized)
    
    cap.release()
    return success

# --- ROUTES ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "lado" and password == "ladokha":
            login_user(User(username))
            return redirect(url_for('home'))
        else:
            flash("Wrong pass")
            return redirect(url_for('login'))
            
    return render_template('login.html')

@app.route('/')
@app.route('/home')
@login_required
def home():
    videos = []
    if VIDEO_PATH.exists():
        for f in os.listdir(VIDEO_PATH):
            if f.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
                generate_thumbnail_opencv(f)
                videos.append({
                    'name': f,
                    'title': Path(f).stem.replace('_', ' ').title(),
                    'thumb': f"{Path(f).stem}.jpg"
                })
    return render_template('home.html', videos=videos)

# THIS WAS THE MISSING ROUTE CAUSING YOUR ERROR
@app.route('/gallery')
@login_required
def gallery():
    images = []
    if IMAGE_PATH.exists():
        for f in os.listdir(IMAGE_PATH):
            if f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
                images.append({
                    'name': f,
                    'title': Path(f).stem.replace('_', ' ').title()
                })
    return render_template('gallery.html', images=images)

@app.route('/video/<path:filename>')
@login_required
def stream_video(filename):
    file_path = VIDEO_PATH / filename
    if not file_path.exists(): abort(404)
    return send_file(file_path, conditional=True)

@app.route('/serve_image/<path:filename>')
@login_required
def serve_image(filename):
    file_path = IMAGE_PATH / filename
    if not file_path.exists(): abort(404)
    return send_file(file_path)

@app.route('/serve_thumb/<path:filename>')
@login_required
def serve_thumb(filename):
    path = THUMB_PATH / filename
    if not path.exists():
        # Look for default image if thumb fails
        default_img = IMAGE_PATH / 'default.jpg'
        return send_file(default_img) if default_img.exists() else abort(404)
    return send_file(path)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)