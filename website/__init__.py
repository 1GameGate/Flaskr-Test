from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from website import dataS

def create_app():
    dataS.count = 1
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'helloworld'
    
    from .views import views
    
    app.register_blueprint(views,url_prefix="/")
    
    return app