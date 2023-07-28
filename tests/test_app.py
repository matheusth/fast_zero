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


def test_update_user_is_workin():
    response = client.put(
        '/users/1',
        json={
            'username': 'string2',
            'email': 'user2@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'string2',
        'email': 'user2@example.com',
    }


def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
