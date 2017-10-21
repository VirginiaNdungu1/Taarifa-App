# initialise flask
from flask import Flask

# import Boostrap class
# from flask_boostrap import Boostrap
# initialise configurations
from config import config_options

# setting up configurations


def create_app(config_name):
    app = Flask(__name__)

    # Create app configurations
    app.config.from_object(config_options[config_name])

    # initialise flask extensions
    # bootstrap.init_app(app)

    # Register the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # set up config_options
    from .requests import configure_request
    configure_request(app)
    '''
    call the configure_request function and pass in the application instance
    Gives access to the application object
    '''

    return app
