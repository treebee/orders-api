import pytest

from orders_api.db.models import Store


@pytest.fixture()
def create_store(db):
    store = Store(
        name="TechStuff Online",
        city="Karlsruhe",
        country="Germany",
        currency="EUR",
        zipcode="76139",
    )
    db.add(store)
    db.flush()
    yield store
    db.rollback()


def test_create(app_client) -> None:
    payload = {
        "name": "Kwik-e Mart",
        "city": "Springfield",
        "country": "USA",
        "currency": "USD",
        "zipcode": "1234",
    }
    rv = app_client.post("/stores/", json=payload)
    assert rv.status_code == 201
    assert rv.json()["name"] == "Kwik-e Mart"


def test_list(app_client, create_store) -> None:
    rv = app_client.get("/stores")
    stores = rv.json()
    assert rv.status_code == 200
    assert len(stores) == 1
    assert stores[0]["name"] == "TechStuff Online"


def test_get(app_client, create_store) -> None:
    rv = app_client.get(f"/stores/{create_store.store_id}")
    stores = rv.json()
    assert rv.status_code == 200
    assert stores["name"] == "TechStuff Online"
