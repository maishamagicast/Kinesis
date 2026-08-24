import os, json
from app.config import Config

DEFAULT_SETTINGS={
    "pinchThreshold":0.05,
    "swipeThreshold":0.15,
    "cooldownMs":800,
    "enableLaserPointer":True,
    "smoothingFactor":0.5
}

def load_settings():
    if not os.path.exists(Config.SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    try:
        with open(Config.SETTINGS_FILE,'r') as f:
            return json.load(f)
    except(json.JSONDecodeError, OSError):
        return DEFAULT_SETTINGS

def save_settings(new_settings):
    os.makedirs(os.path.dirname(Config.SETTINGS_FILE), exist_ok=True)
    
    with open(Config.SETTINGS_FILE,'w') as f:
        json.dump(new_settings,f,indent=2)

    return new_settings