from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login():
    response = client.post("/auth/login", json={"username": "test", "password": "test"})
    assert response.status_code == 200

def test_register():
    response = client.post("/auth/register", json={"name": "test", "email": "test@example.com", "password": "test"})
    assert response.status_code == 200