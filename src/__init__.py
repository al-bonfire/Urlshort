from src import views
from src.models import init_db
from flask import Flask


def create_app(name):
    
    init_db()
    app = Flask(name)
    views.init_app(app)
    
    return app