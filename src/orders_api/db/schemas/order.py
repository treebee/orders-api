from datetime import datetime
from typing import List

from pydantic import BaseModel, Field
from pydantic.types import UUID4

from .product import Product
from .utils import to_camel


class OrderItemCreate(BaseModel):
    product_id: UUID4
    quantity: int = Field(..., gt=0)

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class Order(BaseModel):
    order_id: UUID4
    date: datetime

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


# for order details
class OrderItem(BaseModel):
    quantity: int = Field(..., gt=0)
    product: Product

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


class OrderDetail(Order):
    order_id: UUID4
    date: datetime
    items: List[OrderItem]
