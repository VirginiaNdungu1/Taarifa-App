# initialise flask
from flask import Flask
# initialise configurations
from config import config_options

# setting up configurations


def create_app(config_name):
    app = Flask(__name__)

    # Create app configurations
    app.config.from_object(config_options[config_name])

    return app
