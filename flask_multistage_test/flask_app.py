from example import create_app

app = create_app()

# Flask development server
if '__main__' == __name__:
    app.run(debug=True, host='0.0.0.0')
