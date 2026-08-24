import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))

class Config:
    STATIC_FOLDER=os.path.join(BASE_DIR,'static')
    SLIDES_FOLDER=os.path.join(STATIC_FOLDER,'slides')
    VIDEOS_FOLDER=os.path.join(STATIC_FOLDER,'videos')
    SETTINGS_FILE=os.path.join(BASE_DIR,'user_settings.json')

    ALLOWED_SLIDE_EXTENSIONS={'pdf','json'}
    ALLOWED_VIDEO_EXTENSIONS={'webm','mp4'}

    SECRET_KEY=os.environ.get('SECRET_KEY','dev-secret-key-airdeck-123')
    CORS_ORIGINS=["http://localhost:5173","http://localhost:3000","http://127.0.0.1:5173"]#CORS