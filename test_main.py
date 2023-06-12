from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_response_time():
    response = client.get("/")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() <= 2


def test_random_message_length():
    response = client.get("/random-message")
    assert response.status_code == 200

    message = response.json()["message"]
    assert len(message) < 100
