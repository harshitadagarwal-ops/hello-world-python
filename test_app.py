import pytest
from app import app, elapsed

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World (Python)!' in response.data

def test_elapsed_format():
    result = elapsed()
    assert ':' in result
    parts = result.split(':')
    assert len(parts) == 3



