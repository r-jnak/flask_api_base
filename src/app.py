from flask import Flask
from database import init_db
import models
from controllers import user

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_db(app)

    app.register_blueprint(user.app)

    return app

app = create_app()