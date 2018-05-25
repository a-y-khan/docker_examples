from flask import Flask, render_template
from flask_mongoengine import MongoEngine


db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'testapp1',
    # TODO: set MongoDB host and port information here
    'host': 'mongo',
    'port': 27017
}
db.init_app(app)


@app.route('/')
def hello_world():
    client = db.connection
    server_info = client.server_info()
    return render_template('index.html',
                           connection='{}'.format(client),
                           server_info=server_info)


# Flask development server
if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
