from flask import render_template
from . import bp, db


@bp.route('/')
# @app.route('/')
def hello_world():
    return 'Hello, World!'


@bp.route('/db')
# @app.route('/db')
def server_info():
    client = db.connection
    server_info = client.server_info()
    return render_template('server_info.html',
                           connection='{}'.format(client),
                           server_info=server_info)
