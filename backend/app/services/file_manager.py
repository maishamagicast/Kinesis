import os
from app.config import Config

def get_available_media():
    os.makedirs(Config.SLIDES_FOLDER, exist_ok=True)
    os.makedirs(Config.VIDEOS_FOLDER, exist_ok=True)

    slides=[]
    for filename in os.listdir(Config.SLIDES_FOLDER):
        ext=filename.rsplit('.',1)[-1].lower() if '.' in filename else '' # right split filename, stop after 1 dot and return last item
        if ext in Config.ALLOWED_SLIDE_EXTENSIONS:
            slides.append(
                {
                    "id":filename,
                    "name":filename.rsplit('.',1)[0].replace('_',' ').title(),
                    "url":f"/static/slides/{filename}",
                    "type":ext,
                }
            )

    videos=[]
    for filename in os.listdir(Config.VIDEOS_FOLDER):
            ext=filename.rsplit('.',1)[-1].lower() if '.' in filename else ''
            if ext in Config.ALLOWED_VIDEO_EXTENSIONS:
                slides.append(
                    {
                        "id":filename,
                        "name":filename.rsplit('.',1)[0].replace('_',' ').title(),
                        "url":f"/static/slides/{filename}",
                        "type":ext,
                    }
                )

    return{"slides":slides, "videos":videos}