from .health import health_bp
from .settings import settings_bp
from .media import media_bp

def register_routes(app):
    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(media_bp, url_prefix='/api')
    app.register_blueprint(settings_bp, url_prefix='/api')