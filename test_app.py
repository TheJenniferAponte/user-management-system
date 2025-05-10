import pytest
from app import app, db, User
from datetime import datetime

# Setup the test database
@pytest.fixture
def setup_db():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.create_all()

    # Add test data
    user1 = User(username="john_doe", email="john@example.com", role="admin", status="active", registration_date=datetime(2022, 1, 15))
    user2 = User(username="jane_smith", email="jane@example.com", role="user", status="inactive", registration_date=datetime(2021, 5, 22))
    db.session.add_all([user1, user2])
    db.session.commit()

    yield db

    db.drop_all()

# Test GET all users
def test_get_all_users(setup_db):
    with app.test_client() as client:
        response = client.get('/users')
        data = response.get_json()
        assert response.status_code == 200
        assert len(data) == 2

# Test POST (Create user)
def test_create_user(setup_db):
    with app.test_client() as client:
        response = client.post('/users', json={
            'username': 'new_user',
            'email': 'new@example.com',
            'role': 'admin',
            'status': 'active',
            'registration_date': '2023-01-01'
        })
        data = response.get_json()
        assert response.status_code == 201
        assert data['username'] == 'new_user'

# Test PUT (Update user)
def test_update_user(setup_db):
    with app.test_client() as client:
        # Assume user1 is the user to be updated
        response = client.put('/users/1', json={'username': 'updated_user'})
        data = response.get_json()
        assert response.status_code == 200
        assert data['username'] == 'updated_user'

# Test DELETE (Delete user)
def test_delete_user(setup_db):
    with app.test_client() as client:
        response = client.delete('/users/1')
        assert response.status_code == 200
        assert response.json['message'] == 'User deleted successfully'

# Test error for invalid sort order
def test_invalid_sort_order(setup_db):
    with app.test_client() as client:
        response = client.get('/users?sort_by=username&sort_order=invalid')
        assert response.status_code == 400

# Test error for invalid date format
def test_invalid_date_format(setup_db):
    with app.test_client() as client:
        response = client.get('/users?start_date=2022-01-32')
        assert response.status_code == 400
       assert response.status_code == 400
