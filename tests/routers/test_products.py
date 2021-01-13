import uuid


def test_create(app_client, create_store) -> None:
    payload = {
        "name": "Play Station 6",
        "price": 499.99,
        "storeId": str(create_store.store_id),
    }
    rv = app_client.post("/products/", json=payload)
    assert rv.status_code == 201


def test_create_invalid_store(app_client) -> None:
    payload = {
        "name": "Play Station 6",
        "price": 499.99,
        "storeId": str(uuid.uuid4()),
    }
    rv = app_client.post("/products/", json=payload)
    assert rv.status_code == 400


def test_create_duplicate(app_client, create_product) -> None:
    payload = {
        "name": create_product.name,
        "price": 499.99,
        "storeId": str(create_product.store_id),
    }
    rv = app_client.post("/products/", json=payload)
    assert rv.status_code == 409


def test_list(app_client, create_product) -> None:
    rv = app_client.get("/products")
    products = rv.json()
    assert rv.status_code == 200
    assert len(products) == 1
    assert products[0]["name"] == create_product.name


def test_get(app_client, create_product) -> None:
    rv = app_client.get(f"/products/{create_product.product_id}")
    products = rv.json()
    assert rv.status_code == 200
    assert products["name"] == create_product.name


def test_delete(app_client, create_product) -> None:
    rv = app_client.get(f"/products/{create_product.product_id}")
    assert rv.status_code == 200
    rv = app_client.delete(f"/products/{create_product.product_id}")
    assert rv.status_code == 204
    rv = app_client.get(f"/products/{create_product.product_id}")
    assert rv.status_code == 404


def test_update(app_client, create_product) -> None:
    rv = app_client.patch(
        f"/products/{create_product.product_id}", json={"name": "Rubik's Cube V2"}
    )
    assert rv.status_code == 200
    assert create_product.name == "Rubik's Cube V2"
