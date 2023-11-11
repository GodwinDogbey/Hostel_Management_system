#!/usr/bin/python3
"""
flask setup
"""
import os

from flask import Flask


from web_flask.models.views import views
from web_flask.models.auth import auth
from web_flask.models.staff import staff
from web_flask.models.Rooms import rooms
from web_flask.models.checkin import checkin
from web_flask.models.messaging import messaging
from web_flask.models.Profile import profile
from web_flask.models.reservation import reservation
from web_flask.models.student import student
from web_flask.models.vacation import vacation
from web_flask.models.management import manage


def create_app():
    app = Flask(__name__)
    # database connection
    app.config['SECRET_KEY'] = 'hard to guess string'

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