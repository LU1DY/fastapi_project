from http import HTTPStatus


def test_root_deve_retornar_hello_world(client):
    response = client.get("/")

    assert response.json() == {"message": "Hello World!"}


def test_create_user(client):
    response = client.post(
        "/user/",
        json={
            "username": "chico",
            "password": "francisco.cisco123",
            "email": "chico@francisco.com",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "email": "chico@francisco.com",
        "username": "chico",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "email": "chico@francisco.com",
                "username": "chico",
            }
        ]
    }


def test_update_users(client):
    response = client.put({
        "email": "cisco@francisco.com",
        "username": "batata",
        "password": "123456",
    })

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "email": "cisco@francisco.com",
        "username": "batata",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/user/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "email": "cisco@francisco.com",
        "username": "batata",
        "id": 1,
    }
