import pytest
from fastapi.testclient import TestClient
from src.app import app

def test_get_activities():
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    # Arrange
    client = TestClient(app)
    test_email = "testuser@mergington.edu"
    activity = "Chess Club"
    # Act: Sign up
    signup_resp = client.post(f"/activities/{activity}/signup?email={test_email}")
    # Assert
    assert signup_resp.status_code == 200
    assert f"Signed up {test_email}" in signup_resp.json()["message"]

    # Act: Unregister
    unregister_resp = client.post(f"/activities/{activity}/unregister?email={test_email}")
    # Assert
    assert unregister_resp.status_code == 200
    assert f"Unregistered {test_email}" in unregister_resp.json()["message"]
