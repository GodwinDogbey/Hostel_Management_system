#!/usr/bin/python3

from flask import Blueprint, render_template

manage = Blueprint('manage', __name__)


@manage.route('/block')
def BlockManage():
    return render_template('manageBlock.html')


@manage.route('/rooms')
def Rooms():
    return render_template('rooms.html')


@manage.route('/roomstype')
def RoomType():
    return render_template('rooms.html')


@manage.route('/configure')
def configure():
    return render_template('configure.html')


@manage.route('/expiry')
def expiry():
    return render_template('expiry.html')


