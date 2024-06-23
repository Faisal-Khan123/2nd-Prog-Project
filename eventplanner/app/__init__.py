from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_mail import Mail

# Initialize SQLAlchemy and Mail instances
db = SQLAlchemy()
mail = Mail()

def create_app():
    """
    Function to create a Flask application instance and configure it.
    Returns:
        app (Flask): Configured Flask application instance
    """
    app = Flask(__name__)

    # Configure Flask app settings
    app.config['SECRET_KEY'] = 'tech@786929'  # Change this to a random secret key
    app.config['SESSION_TYPE'] = 'filesystem'  # Store session files on disk

    # Configure SQLAlchemy database URI and tracking modifications
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/faisa/OneDrive/Desktop/Project II/env/env/eventplanner/eventplanner/instance/eventplanner.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure Flask-Mail settings for sending emails
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'smith786tom@gmail.com'  # Replace with your email
    app.config['MAIL_PASSWORD'] = 'Smithtom1'  # Replace with your email password
    app.config['MAIL_DEFAULT_SENDER'] = ('Event Planner', 'smith786tom@gmail.com')

    # Initialize SQLAlchemy and Mail with the Flask application instance
    db.init_app(app)
    mail.init_app(app)

    # Create all database tables defined in app.models
    with app.app_context():
        from app.models import User, Event, Feedback
        db.create_all()

    # Register Blueprint(s) for routes
    from app.routes import main
    app.register_blueprint(main)

    return app
