#!/usr/bin/python3
"""
flask setup
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .views import views
from .auth import auth
from .staff import staff
from .Rooms import rooms
from .checkin import checkin
from .messaging import messaging
from .Profile import profile
from .reservation import reservation
from .student import student
from .vacation import vacation
from .management import manage

db = SQLAlchemy()
user = os.getenv('FLASK_DB_USER')
passwd = os.getenv('FLASK_DB_PWD')
host = os.getenv('FLASK_DB_HOST')
database = os.getenv('FLASK_DB__DB')

def create_app():
    app = Flask(__name__)
    # database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{user}:{passwd}@{host}/{database}'
    app.config['SECRET_KEY'] = 'hard to guess string'
    db.init_app(app)

    # blueprint registration
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(staff, url_prefix='/')
    app.register_blueprint(messaging, url_prefix='/')
    app.register_blueprint(rooms, url_prefix='/')
    app.register_blueprint(student, url_prefix='/')
    app.register_blueprint(checkin, url_prefix='/')
    app.register_blueprint(profile, url_prefix='/')
    app.register_blueprint(vacation, url_prefix='/')
    app.register_blueprint(reservation, url_prefix='/')
    app.register_blueprint(manage, url_prefix='/')


    return app