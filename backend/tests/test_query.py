from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_invalid_input():
    # إرسال body فارغ أو غير متوافق لنتوقع كود 422
    response = client.post("/query", json={})
    assert response.status_code == 422
    