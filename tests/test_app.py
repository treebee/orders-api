from fastapi.testclient import TestClient


def test_health(app_client: TestClient) -> None:
    rv = app_client.get("/health")
    assert rv.status_code == 200
