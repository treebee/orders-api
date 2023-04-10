from fastapi.testclient import TestClient

from orders_api.db.models import Store


def test_create(app_client: TestClient) -> None:
    payload = {
        "name": "Kwik-e Mart",
        "city": "Springfield",
        "country": "USA",
        "currency": "USD",
        "zipcode": "1234",
        "street": "First Street",
    }
    rv = app_client.post("/stores/", json=payload)
    assert rv.status_code == 201
    assert rv.json()["name"] == "Kwik-e Mart"
    assert rv.json()["storeId"] is not None


def test_list(app_client: TestClient, create_store: Store) -> None:
    rv = app_client.get("/stores")
    stores = rv.json()
    assert rv.status_code == 200
    assert len(stores) == 1
    assert stores[0]["name"] == create_store.name


def test_get(app_client: TestClient, create_store: Store) -> None:
    rv = app_client.get(f"/stores/{create_store.store_id}")
    stores = rv.json()
    assert rv.status_code == 200
    assert stores["name"] == "TechStuff Online"


def test_delete(app_client: TestClient, create_store: Store) -> None:
    rv = app_client.get(f"/stores/{create_store.store_id}")
    assert rv.status_code == 200
    rv = app_client.delete(f"/stores/{create_store.store_id}")
    assert rv.status_code == 204
    rv = app_client.get(f"/stores/{create_store.store_id}")
    assert rv.status_code == 404


def test_update(app_client: TestClient, create_store: Store) -> None:
    rv = app_client.patch(
        f"/stores/{create_store.store_id}", json={"name": "New Store Name"}
    )
    assert rv.status_code == 204
    rv = app_client.get(f"/stores/{create_store.store_id}")
    assert rv.json()["name"] == "New Store Name"
