import decimal
import uuid
from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import RelationshipProperty, registry, relationship
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy_utils import EmailType

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata

    __init__ = mapper_registry.constructor


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
    email: Optional[EmailType] = sa.Column(EmailType)


class Product(Base):
    __tablename__ = "products"
    __allow_unmapped__ = True

    product_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_id = sa.Column(ForeignKey("stores.store_id"), nullable=False)
    store: RelationshipProperty[Store] = relationship("Store", backref="products")
    name = sa.Column(sa.Text, nullable=False)
    price = sa.Column(sa.Numeric(12, 2), nullable=False)
    description = sa.Column(sa.Text)

    __table_args__ = (UniqueConstraint("name", "store_id", name="uix_products"),)


class Order(Base):
    __tablename__ = "orders"
    __allow_unmapped__ = True

    order_id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    items: List["OrderItem"] = relationship("OrderItem", backref="order")  # type: ignore

    @hybrid_property
    def total(self) -> decimal.Decimal:
        total_price = decimal.Decimal("0.0")
        for item in self.items:
            total_price += decimal.Decimal(item.product.price * item.quantity)
        return total_price


class OrderItem(Base):
    __tablename__ = "order_items"
    __allow_unmapped__ = True

    order_id = sa.Column(ForeignKey("orders.order_id"), primary_key=True)
    product_id = sa.Column(ForeignKey("products.product_id"), primary_key=True)
    product: RelationshipProperty[Product] = relationship("Product", uselist=False)
    quantity = sa.Column(sa.Integer, nullable=False)
