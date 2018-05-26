import pytest

from flask_app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.debug = True
    #return app.test_client()
    return app


def test_hello_world(app):
    res = app.test_client().get('/')
    # res = app.client().get('/')
    print(res.status_code)
    assert res.status_code == 200
    assert b'Hello, World!' in res.data


def test_db(app):
    res = app.test_client().get('/db')
    print(res.status_code)
    assert res.status_code == 200
    # TODO: check data