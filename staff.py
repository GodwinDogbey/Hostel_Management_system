#!/usr/bin/python3

from flask import Blueprint, render_template

staff = Blueprint('staff', __name__)


@staff.route('/staff')
def  users():
    # Creating dummy data
    users = [
        {"name": "John Doe", "email": "john.doe@example.com", "role": "Manager"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "role": "Engineer"},
        {"name": "Bob Johnson", "email": "bob.johnson@example.com", "role": "Designer"},
        {"name": "Alice Brown", "email": "alice.brown@example.com", "role": "Analyst"}
    ]

    return render_template('manageStaff.html', users=users)
