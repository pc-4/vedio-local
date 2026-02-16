import os
import subprocess
import socket
from flask import Flask, render_template, send_from_directory, request
import urllib.parse

app = Flask(__name__)

# Correct Folder Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
VIDEO_DIR = os.path.join(ASSETS_DIR, 'vedios')
THUMB_DIR = os.path.join(ASSETS_DIR, 'thubnail')
IMAGE_DIR = os.path.join(ASSETS_DIR, 'image')

# Create folders if missing
for d in [VIDEO_DIR, THUMB_DIR, IMAGE_DIR]:
    os.makedirs(d, exist_ok=True)

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError: return False

def generate_thumb(video_name):
    # This replaces spaces with underscores for the thumbnail filename to avoid errors
    clean_name = video_name.replace(" ", "_")
    thumb_name = os.path.splitext(clean_name)[0] + ".jpg"
    thumb_path = os.path.join(THUMB_DIR, thumb_name)
    video_path = os.path.join(VIDEO_DIR, video_name)
    
    if not os.path.exists(thumb_path):
        try:
            # Force FFmpeg to run. If this fails, no thumbnail is created.
            subprocess.run([
                'ffmpeg', '-i', video_path, '-ss', '00:00:02', 
                '-vframes', '1', thumb_path
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Thumbnail error: {e}")
            return None
    return thumb_name

@app.route('/')
def home():
    video_files = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(('.mp4', '.mkv', '.mov'))]
    videos = []
    for f in video_files:
        t = generate_thumb(f)
        videos.append({'name': f, 'thumb': t if t else "default.jpg"})
    return render_template('index.html', items=videos, online=is_connected(), mode="video")

@app.route('/images')
def images():
    img_files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    return render_template('index.html', items=img_files, online=is_connected(), mode="image")

@app.route('/assets/<path:folder>/<path:filename>')
def serve_file(folder, filename):
    # This handles spaces in filenames correctly
    return send_from_directory(os.path.join(ASSETS_DIR, folder), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)