from orders_api.db.models import Product


def test_create(app_client, create_product: Product) -> None:
    payload = {"items": [{"productId": str(create_product.product_id), "quantity": 2}]}
    rv = app_client.post("/orders/", json=payload)
    assert rv.status_code == 201, rv.text


def test_list(app_client, create_order) -> None:
    rv = app_client.get("/orders")
    orders = rv.json()
    assert rv.status_code == 200
    assert len(orders) == 1
    assert orders[0]["orderId"] == str(create_order.order_id)


def test_get(app_client, create_order) -> None:
    rv = app_client.get(f"/orders/{create_order.order_id}")
    assert rv.status_code == 200
    assert "date" in rv.json()
    assert rv.json()["items"][0]["quantity"] == create_order.items[0].quantity
