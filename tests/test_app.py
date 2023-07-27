from fastapi.testclient import TestClient
from fast_zero.app import app

client = TestClient(app)


def test_root_should_return_200_ok_and_ola_mundo():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá mundo!'}
