from src.views import router
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(router.bp, url_prefix='/flask')