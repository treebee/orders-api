from decimal import Decimal
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session
from sqlalchemy_utils import create_database, database_exists

from orders_api.app import create_app
from orders_api.db.models import Base, Order, OrderItem, Product, Store
from orders_api.db.session import create_session


@pytest.fixture(scope="session")
def db() -> scoped_session:
    db_session: scoped_session = create_session()
    assert db_session.bind is not None
    engine: Engine = db_session.bind.engine
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return db_session


@pytest.fixture()
def cleanup_db(db: scoped_session) -> None:
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())


@pytest.fixture()
def app_client(cleanup_db: Any) -> Generator[TestClient, None, None]:
    app = create_app()
    yield TestClient(app)


@pytest.fixture()
def create_store(db: scoped_session) -> Generator[Store, None, None]:
    store = Store(
        name="TechStuff Online",
        city="Karlsruhe",
        country="Germany",
        currency="EUR",
        zipcode="76131",
        street="Kaiserstr. 42",
    )
    db.add(store)
    db.commit()
    yield store


@pytest.fixture()
def create_product(
    db: scoped_session, create_store: Store
) -> Generator[Product, None, None]:
    product = Product(
        name="Rubik's Cube", price=Decimal("9.99"), store_id=create_store.store_id
    )
    db.add(product)
    db.commit()
    yield product


@pytest.fixture()
def create_order(
    db: scoped_session, create_product: Product
) -> Generator[Order, None, None]:
    order = Order()
    db.add(order)
    db.commit()
    order_item = OrderItem(
        product_id=create_product.product_id, order_id=order.order_id, quantity=2
    )
    db.add(order_item)
    db.commit()
    yield order
