import pytest
from app import app as flask_app, database

@pytest.fixture(scope='session')
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup: Ensure the database is clean before each test
    with flask_app.app_context():
        database.create_table()
    yield
    # Teardown: Clean up if necessary (e.g., delete rows but do not close the connection)
    with flask_app.app_context():
        database.conn.execute('DELETE FROM results')
        database.conn.commit()
