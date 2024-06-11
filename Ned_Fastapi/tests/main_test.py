from fastapi.testclient import TestClient
from ned_fastapi.main import app

client : TestClient = TestClient(app=app)

def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}