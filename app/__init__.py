from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    from main import main_blueprint
    app.register_blueprint(main_blueprint)

    # setting the config
    from .requests import configure_request
    configure_request(app)

    return app