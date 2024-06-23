import pytest
from app import create_app, db
from app.models import User, Event, Feedback

# Fixture to provide a test client for Flask app
@pytest.fixture(scope='module')
def test_client():
    # Create the Flask app instance for testing
    flask_app = create_app()

    # Configure the app for testing
    flask_app.config['TESTING'] = True  # Set to True to enable testing mode
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite database for testing

    # Create a test client using Flask's built-in test client
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            # Set up the database schema
            db.create_all()
            yield testing_client  # Provide the client to the tests

    # Clean up after tests
    with flask_app.app_context():
        db.drop_all()  # Drop all tables after testing

# Fixture to initialize the database with test data
@pytest.fixture(scope='module')
def init_database():
    # Create a new user for testing
    user = User(username='testuser', email='testuser@example.com', password='testpassword')
    db.session.add(user)
    db.session.commit()
    return user  # Provide the user object to tests that need it
