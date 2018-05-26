import pytest

from flask_app import create_app


# from http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.debug = True
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_hello_world(test_client):
    res = test_client.get('/')
    assert res.status_code == 200
    assert b'Hello, World!' in res.data


def test_db(test_client):
    res = test_client.get('/db')
    assert res.status_code == 200
    assert b'Mongo Server Information' in res.data