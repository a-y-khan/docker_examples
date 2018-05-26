from flask import Flask, render_template
from flask_mongoengine import MongoEngine


# TODO: best practice is to put this in a database models.py
db = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'testapp1',
        'host': 'mongo',
        'port': 27017
    }
    db.init_app(app)
    return app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db')
def server_info():
    client = db.connection
    server_info = client.server_info()
    return render_template('server_info.html',
                           connection='{}'.format(client),
                           server_info=server_info)


# Flask development server
if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
