from flask import Flask, Blueprint
from flask_mongoengine import MongoEngine


bp = Blueprint('flask_app', __name__, template_folder='templates')

# TODO: best practice is to put this in a database models.py
db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'testapp1',
        'host': 'mongo',
        'port': 27017
    }
    db.init_app(app)
    return app

from . import routes