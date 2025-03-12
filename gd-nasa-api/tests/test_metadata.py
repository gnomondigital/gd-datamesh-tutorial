from fastapi.testclient import TestClient

from src.gd_nasa_api.main import app


client = TestClient(app)


def test_healthz_positive():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_get_metadata_positive():
    response = client.get("/metadata")
    assert response.status_code == 200
    assert response.json() == {
        "name": "gd-nasa-api",
        "description": "Exposing nasa opendata using an api",
    }
