from flask import session, render_template, Blueprint, jsonify, request, redirect, url_for, make_response
from app.models import db, User, Event, Feedback
from flask_mail import Mail, Message
import plotly.graph_objects as go
import base64
from flask import render_template
from app import mail

from datetime import datetime

# Define a Blueprint named 'main' for grouping related routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    events = Event.query.all()  # Retrieve all events from the database
    return render_template('index.html', events=events)

@main.route('/register-form')
def create_account():
    return render_template('register.html')  # Render the registration form

@main.route('/register', methods=['POST'])
def register():
    data = request.form
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)  # Add new user to the database
    db.session.commit()  # Commit the transaction
    return redirect(url_for('main.index'))  # Redirect to the index page

@main.route('/login-form')
def login_form():
    return render_template('login.html')  # Render the login form

@main.route('/login', methods=['POST'])
def login():
    data = request.form
    user = User.query.filter_by(email=data['email']).first()  # Retrieve user by email
    if user and user.password == data['password']:
        session['user_id'] = user.id  # Store user ID in the session
        response = make_response(redirect(url_for('main.home')))
        return response
    return jsonify({'message': 'Invalid credentials'}), 401  # Return error if login fails

@main.route('/home')
def home():
    events = Event.query.all()  # Retrieve all events
    return render_template('home.html', events=events)  # Render the home page with events

@main.route('/add-event')
def add_event_form():
    return render_template('add_event.html')  # Render the add event form

@main.route('/add-event-db', methods=['POST'])
def add_event():
    if 'user_id' not in session:
        return jsonify({'message': 'User not logged in'}), 401  # Check if user is logged in
    
    data = request.form
    date_str = data['date']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()  # Convert date string to date object

    new_event = Event(
        title=data['title'],
        description=data['description'],
        date=date_obj,
        location=data['location'],
        user_id=session['user_id']  # Get user ID from the session
    )
    
    db.session.add(new_event)  # Add new event to the database
    db.session.commit()  # Commit the transaction
    return redirect(url_for('main.home'))  # Redirect to the home page

@main.route('/update_event_form')
def update_form():
    return render_template('update_event.html')  # Render the update event form

@main.route('/update-event', methods=['POST'])
def update_event():
    data = request.form
    event_id = data.get('event_id')
    
    if not event_id:
        return jsonify({'message': 'Valid event ID is required'}), 400  # Check for valid event ID
    
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404  # Check if event exists

    event.title = data.get('title')
    event.description = data.get('description')
    event.date = datetime.strptime(data.get('date'), '%Y-%m-%d').date()
    event.location = data.get('location')
    
    db.session.commit()  # Commit the updates
    return redirect(url_for('main.home'))  # Redirect to the home page

@main.route('/delete_event_form')
def delete_form():
    return render_template('delete_event_ui.html')  # Render the delete event form

@main.route('/delete-event', methods=['POST'])
def delete_event():
    data = request.form
    event_id = data.get('event_id')
    
    if not event_id:
        return jsonify({'message': 'Event ID is required'}), 400  # Check for valid event ID
    
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404  # Check if event exists

    db.session.delete(event)  # Delete the event
    db.session.commit()  # Commit the transaction
    return redirect(url_for('main.home'))  # Redirect to the home page

@main.route('/fdbck_form')
def feedback_form():
    return render_template('feedback_form.html')  # Render the feedback form

@main.route('/add-fdbck-db', methods=['POST'])
def add_feedback():
    data = request.form
    date_obj = datetime.now()  # Get current date and time

    new_feedback = Feedback(
        title=data['event_title'],
        email=data['user_mail'],
        date=date_obj,
        feedback=data['feedback'],
    )
    
    db.session.add(new_feedback)  # Add new feedback to the database
    db.session.commit()  # Commit the transaction
    return redirect(url_for('main.show_feedbacks'))  # Redirect to show feedbacks

@main.route('/survey_feedbacks')
def show_feedbacks():
    feedbacks = Feedback.query.all()  # Retrieve all feedbacks
    return render_template('feedbacks.html', feedbacks=feedbacks)  # Render the feedbacks page

@main.route('/logout')
def logout():
    response = redirect(url_for('main.index'))  # Redirect to index page
    response.set_cookie('access_token', '', expires=0)  # Clear access token cookie
    return response

@main.route('/register-for-event', methods=['POST'])
def register_for_event():
    data = request.json  # Assuming data is sent as JSON in the request body
    event_id = data.get('eventId')
    email = data.get('email')

    # Fetch event details based on event_id
    event = Event.query.get(event_id)

    if not event:
        return jsonify({'success': False, 'message': 'Event not found'}), 404

    # Register user for the event (this is a simple example, adjust as necessary)
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(username=email.split('@')[0], email=email, password='defaultpassword')
        db.session.add(user)
        db.session.commit()

    # Prepare email message
    msg = Message(
        subject='You have been registered for an event!',
        recipients=[email],
        body=f'You have successfully registered for the event "{event.title}".\n\nEvent details:\n\nDescription: {event.description}\nDate: {event.date}\nLocation: {event.location}'
    )

    try:
        mail.send(msg)  # Send the email
        return jsonify({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        print(str(e))  # Print the error for debugging purposes
        return jsonify({'success': False, 'message': 'Failed to send email'}), 500

@main.route('/stats')
def stats():
    user_count = User.query.count()  # Get count of users
    feedback_count = Feedback.query.count()  # Get count of feedbacks
    
    labels = ['Users', 'Feedbacks']
    values = [user_count, feedback_count]

    # Create a pie chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial')])

    # Use Kaleido for exporting the image
    img_bytes = fig.to_image(format="png", engine="kaleido")
    img_base64 = base64.b64encode(img_bytes).decode('utf8')  # Encode image to base64

    return render_template('stats.html', img_data=img_base64)  # Render the stats page with the chart
