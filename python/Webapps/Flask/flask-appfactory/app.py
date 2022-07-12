from flask import Flask
from config import Config


def create_app():

    app = Flask(__name__)
    
    app.config.from_object(Config)

    app.register_blueprint(admin)

    return app



# el comando flask run, detectara automaticamente que la factory existe