# from flask import Flask, Blueprint, render_template
# from flask_mongoengine import MongoEngine
#
#
# bp = Blueprint('flask_app', __name__)
# from . import routes
#
# # TODO: best practice is to put this in a database models.py
# db = MongoEngine()
#
# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(bp)
#     app.config['MONGODB_SETTINGS'] = {
#         'db': 'testapp1',
#         'host': 'mongo',
#         'port': 27017
#     }
#     db.init_app(app)
#     return app
#
#
# app = create_app()
#
#
# @bp.route('/')
# # @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# @bp.route('/db')
# # @app.route('/db')
# def server_info():
#     client = db.connection
#     server_info = client.server_info()
#     return render_template('server_info.html',
#                            connection='{}'.format(client),
#                            server_info=server_info)


from example import create_app

app = create_app()

# Flask development server
if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
