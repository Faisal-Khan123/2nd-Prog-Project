import json
from app.models import User, Event, Feedback
from datetime import datetime
from app import db

def test_index(test_client):
    # Test the index route to ensure it loads correctly
    response = test_client.get('/')
    assert response.status_code == 200
    # Check if the response contains the expected text
    assert b'Following Events Are Available' in response.data or b'No active events at the moment' in response.data

def test_create_account(test_client):
    # Test the route to load the account creation form
    response = test_client.get('/register-form')
    assert response.status_code == 200

def test_register(test_client):
    # Test the registration functionality
    response = test_client.post('/register', data={
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 302  # Redirect status code
    # Verify the user was added to the database
    user = User.query.filter_by(email='newuser@example.com').first()
    assert user is not None

def test_login_form(test_client):
    # Test the route to load the login form
    response = test_client.get('/login-form')
    assert response.status_code == 200

def test_login(test_client, init_database):
    # Test the login functionality
    response = test_client.post('/login', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 302  # Redirect status code

def test_add_event_form(test_client, init_database):
    # Test the route to load the add event form
    with test_client.session_transaction() as sess:
        sess['user_id'] = init_database.id

    response = test_client.get('/add-event')
    assert response.status_code == 200

def test_add_event(test_client, init_database):
    # Test the functionality to add a new event
    with test_client.session_transaction() as sess:
        sess['user_id'] = init_database.id

    response = test_client.post('/add-event-db', data={
        'title': 'New Event',
        'description': 'This is a new event.',
        'date': '2024-06-30',
        'location': 'Test Location'
    })
    assert response.status_code == 302  # Redirect status code
    # Verify the event was added to the database
    event = Event.query.filter_by(title='New Event').first()
    assert event is not None

def test_update_event(test_client, init_database):
    # Setup: Add an event to update
    event = Event(
        title='Event to Update',
        description='Event description.',
        date=datetime.strptime('2024-07-01', '%Y-%m-%d').date(),
        location='Test Location',
        user_id=init_database.id
    )
    db.session.add(event)
    db.session.commit()

    # Test the update functionality
    response = test_client.post('/update-event', data={
        'event_id': event.id,
        'title': 'Updated Event',
        'description': 'Updated description.',
        'date': '2024-07-01',
        'location': 'Updated Location'
    })
    assert response.status_code == 302  # Redirect status code
    # Verify the event was updated in the database
    updated_event = Event.query.get(event.id)
    assert updated_event.title == 'Updated Event'

def test_delete_event(test_client, init_database):
    # Setup: Add an event to delete
    event = Event(
        title='Event to Delete',
        description='Event description.',
        date=datetime.strptime('2024-07-01', '%Y-%m-%d').date(),
        location='Test Location',
        user_id=init_database.id
    )
    db.session.add(event)
    db.session.commit()

    # Test the delete functionality
    response = test_client.post('/delete-event', data={'event_id': event.id})
    assert response.status_code == 302  # Redirect status code
    # Verify the event was deleted from the database
    deleted_event = Event.query.get(event.id)
    assert deleted_event is None

def test_feedback_form(test_client):
    # Test the route to load the feedback form
    response = test_client.get('/fdbck_form')
    assert response.status_code == 200

def test_add_feedback(test_client):
    # Test the functionality to add feedback
    response = test_client.post('/add-fdbck-db', data={
        'event_title': 'Event Title',
        'user_mail': 'feedbackuser@example.com',
        'feedback': 'This is a feedback.'
    })
    assert response.status_code == 302  # Redirect status code
    # Verify the feedback was added to the database
    feedback = Feedback.query.filter_by(email='feedbackuser@example.com').first()
    assert feedback is not None

def test_show_feedbacks(test_client):
    # Test the route to display feedbacks
    response = test_client.get('/survey_feedbacks')
    assert response.status_code == 200

def test_register_for_event(test_client, init_database):
    # Setup: Add an event to register for
    event = Event(
        title='Event for Registration',
        description='Event description.',
        date=datetime.strptime('2024-07-01', '%Y-%m-%d').date(),
        location='Test Location',
        user_id=init_database.id
    )
    db.session.add(event)
    db.session.commit()

    # Test the functionality to register for an event
    response = test_client.post('/register-for-event', json={
        'eventId': event.id,
        'email': 'registeruser@example.com'
    })
    assert response.status_code == 200
    # Verify the response contains success message
    data = json.loads(response.data)
    assert data['success'] is True

def test_stats(test_client):
    # Test the stats route
    response = test_client.get('/stats')
    assert response.status_code == 200
