# import Blueprint class
from flask import Blueprint
# initialise the Blueprint class
main = Blueprint('main', __name__)
# import views module
from . import views
