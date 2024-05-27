import pytest
from Flask-application.app import app  # Adjust the import to match your package structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to my Application" in response.data
