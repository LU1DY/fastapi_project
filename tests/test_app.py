from fastapi.testclient import TestClient

from fast_api_projeto.app import app

client = TestClient(app)


def test_root_deve_retornar_hello_world():
    response = client.get("/")

    assert response.json() == {"message": "Hello World!"}
