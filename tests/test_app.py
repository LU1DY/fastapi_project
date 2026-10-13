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
                "username": "chico",
                "id": 1,
                "email": "chico@francisco.com",
            }
        ]
    }


def test_get_user_negative(client):
    response = client.get("/user/-1")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}


def test_get_user_no_such(client):
    response = client.get("/user/99999")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}


def test_get_user(client):
    response = client.get("/user/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "chico",
        "email": "chico@francisco.com",
        "id": 1,
    }


def test_update_users(client):
    response = client.put(
        "/user/1",
        json={
            "email": "cisco@francisco.com",
            "username": "batata",
            "password": "123456",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "email": "cisco@francisco.com",
        "username": "batata",
        "id": 1,
    }


def test_update_negative_id(client):
    response = client.put(
        "/user/-1",
        json={
            "email": "cisco@francisco.com",
            "username": "batata",
            "password": "123456",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}


def test_update_no_such_id(client):
    response = client.put(
        "/user/9000",
        json={
            "email": "cisco@francisco.com",
            "username": "batata",
            "password": "123456",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}


def test_delete_user(client):
    response = client.delete("/user/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "email": "cisco@francisco.com",
        "username": "batata",
        "id": 1,
    }


def test_delete_negative_id(client):
    response = client.delete("/user/-1")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}


def test_delete_no_such_id(client):
    response = client.delete("/user/9000")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "Usuário não encontrado!"}
