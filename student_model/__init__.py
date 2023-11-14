from flask import Blueprint

student_views = Blueprint('student_views', __name__, template_folder='student_templates', static_folder='student_static')
from web_flask.student_model.defualt import *