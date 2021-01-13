from decimal import Decimal
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

from orders_api.app import create_app
from orders_api.db.models import Base, Order, OrderItem, Product, Store
from orders_api.db.session import create_session


@pytest.fixture(scope="session")
def db() -> Session:
    db_session = create_session()
    engine = db_session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all()
    return db_session


@pytest.fixture()
def cleanup_db(db: Session) -> None:
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())


@pytest.fixture()
def app_client(cleanup_db: Any) -> Generator[TestClient, None, None]:
    app = create_app()
    yield TestClient(app)


@pytest.fixture()
def create_store(db: Session) -> Generator[Store, None, None]:
    store = Store(
        name="TechStuff Online",
        city="Karlsruhe",
        country="Germany",
        currency="EUR",
        zipcode="76131",
        street="Kaiserstr. 42",
    )
    db.add(store)
    db.flush()
    yield store
    db.rollback()


@pytest.fixture()
def create_product(db: Session, create_store: Store) -> Generator[Product, None, None]:
    product = Product(
        name="Rubik's Cube", price=Decimal("9.99"), store_id=create_store.store_id
    )
    db.add(product)
    db.flush()
    yield product
    db.rollback()


@pytest.fixture()
def create_order(db: Session, create_product: Product) -> Generator[Order, None, None]:
    order = Order()
    db.add(order)
    db.flush()
    order_item = OrderItem(
        product_id=create_product.product_id, order_id=order.order_id, quantity=2
    )
    db.add(order_item)
    db.flush()
    yield order
    db.rollback()
