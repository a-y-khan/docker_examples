from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Flask development server
if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
