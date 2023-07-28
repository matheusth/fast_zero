from fastapi.testclient import TestClient
from fast_zero.app import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        '/users/',
        json={
            'username': 'string',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'string',
        'email': 'user@example.com',
    }


def test_list_users():
    response = client.get('/users/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [{'id': 1, 'username': 'string', 'email': 'user@example.com'}]
    }
