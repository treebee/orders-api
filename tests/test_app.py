def test_health(app_client):
    rv = app_client.get("/health")
    assert rv.status_code == 200
