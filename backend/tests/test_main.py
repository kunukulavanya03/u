from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app.schemas import UserCreate, User
from app.crud import get_user, get_users, create_user, update_user, delete_user
from app.dependencies import get_db
from app.database import SessionLocal
from app.settings import settings

client = TestClient(app)

def test_get_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_get_users():
    response = client.get('/users')
    assert response.status_code == 401


def test_create_user():
    user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
    response = client.post('/users', json=user_data)
    assert response.status_code == 201
    assert response.json()['username'] == user_data['username']
    assert response.json()['email'] == user_data['email']


def test_get_user():
    user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
    user = create_user(get_db(), user_data)
    response = client.get(f'/users/{user.id}')
    assert response.status_code == 401


def test_update_user():
    user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
    user = create_user(get_db(), user_data)
    updated_user_data = {'username': 'updatedtestuser', 'email': 'updatedtest@example.com'}
    response = client.put(f'/users/{user.id}', json=updated_user_data)
    assert response.status_code == 401
    assert response.json()['username'] == updated_user_data['username']
    assert response.json()['email'] == updated_user_data['email']


def test_delete_user():
    user_data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
    user = create_user(get_db(), user_data)
    response = client.delete(f'/users/{user.id}')
    assert response.status_code == 401