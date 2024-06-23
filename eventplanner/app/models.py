from app import db  # Import the SQLAlchemy instance

class User(db.Model):
    # Define the User model with SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for User
    username = db.Column(db.String(150), nullable=False)  # Username column, max length 150, not nullable
    email = db.Column(db.String(150), unique=True, nullable=False)  # Email column, unique and not nullable
    password = db.Column(db.String(150), nullable=False)  # Password column, not nullable

class Event(db.Model):
    # Define the Event model with SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for Event
    title = db.Column(db.String(150), nullable=False)  # Title column, max length 150, not nullable
    description = db.Column(db.Text, nullable=False)  # Description column as text, not nullable
    date = db.Column(db.DateTime, nullable=False)  # Date column as datetime, not nullable
    location = db.Column(db.String(150), nullable=False)  # Location column, max length 150, not nullable
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User table

class Feedback(db.Model):
    # Define the Feedback model with SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for Feedback
    title = db.Column(db.String(150), nullable=False)  # Title column, max length 150, not nullable
    feedback = db.Column(db.Text, nullable=False)  # Feedback column as text, not nullable
    date = db.Column(db.DateTime, nullable=False)  # Date column as datetime, not nullable
    email = db.Column(db.String(150), nullable=False)  # Email column, max length 150, not nullable
