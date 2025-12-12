from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"title": "test", "description": "test"})
    assert response.status_code == 200

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200

def test_update_item():
    response = client.put("/items/1", json={"title": "test", "description": "test"})
    assert response.status_code == 200

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200