import uuid
from typing import Any

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy_utils import EmailType

Base: Any = declarative_base()


class Store(Base):
    __tablename__ = "stores"

    store_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    city = sa.Column(sa.Text, nullable=False)
    country = sa.Column(sa.Text, nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    domain = sa.Column(sa.Text)
    name = sa.Column(sa.Text, nullable=False)
    phone = sa.Column(sa.Text)
    street = sa.Column(sa.Text, nullable=False)
    zipcode = sa.Column(sa.Text, nullable=False)
    email = sa.Column(EmailType)


class Product(Base):
    __tablename__ = "products"

    product_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = sa.Column(ForeignKey("stores.store_id"), nullable=False)
    store = relationship("Store", backref="products")
    name = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.Numeric(12, 2), nullable=False)
    description = sa.Column(sa.Text)

    __table_args__ = (UniqueConstraint("name", "store_id", name="uix_products"),)


class Order(Base):
    __tablename__ = "orders"

    order_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    items = relationship("OrderItem", backref="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id = sa.Column(ForeignKey("orders.order_id"), primary_key=True)
    product_id = sa.Column(ForeignKey("products.product_id"), primary_key=True)
    product = relationship("Product", uselist=False)
    quantity = sa.Column(sa.Integer, nullable=False)
