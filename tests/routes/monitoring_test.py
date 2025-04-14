import os

from fastapi.testclient import TestClient

os.environ['ANNOTATIONS'] = 'annotation1:value1'

from app.main import app

client = TestClient(app)


def test_when_get_health_is_called_then_healthy_status_is_returned():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'healthy'}
