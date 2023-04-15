from fastapi.testclient import TestClient

from orders_api.db.models import Order, Product


def test_create(app_client: TestClient, create_product: Product) -> None:
    payload = {"items": [{"productId": str(create_product.product_id), "quantity": 2}]}
    rv = app_client.post("/orders/", json=payload)
    assert rv.status_code == 201, rv.text


def test_list(app_client: TestClient, create_order: Order) -> None:
    rv = app_client.get("/orders")
    orders = rv.json()
    assert rv.status_code == 200
    assert len(orders) == 1
    assert orders[0]["orderId"] == str(create_order.order_id)
    assert orders[0]["total"] == 9.99 * 2


def test_get(app_client: TestClient, create_order: Order) -> None:
    rv = app_client.get(f"/orders/{create_order.order_id}")
    assert rv.status_code == 200
    assert "date" in rv.json()
    assert rv.json()["items"][0]["quantity"] == create_order.items[0].quantity
