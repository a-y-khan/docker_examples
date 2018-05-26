import pytest

from flask_app import create_app


# from http://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.debug = True
    # return app.test_client()
    testing_client = flask_app.test_client()
    print(testing_client)
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
    # return flask_app


def test_hello_world(test_client):
    res = test_client.get('/')
    print(res.status_code)
    assert res.status_code == 200
    assert b'Hello, World!' in res.data


def test_db(test_client):
    res = test_client.get('/db')
    print(res.status_code)
    assert res.status_code == 200
    # TODO: check data