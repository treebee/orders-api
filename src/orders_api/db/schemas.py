from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl
from pydantic.types import UUID4, condecimal, constr


def to_camel(string: str) -> str:
    if "_" not in string:
        return string
    words = string.split("_")
    words = [words[0]] + [word.capitalize() for word in words[1:]]
    return "".join(words)


class StoreBase(BaseModel):
    name: Optional[str]
    city: Optional[str]
    country: Optional[str]
    currency: Optional[constr(min_length=3, max_length=3)]  # type: ignore
    domain: Optional[HttpUrl]
    phone: Optional[str]
    street: Optional[str]
    zipcode: Optional[str]

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class StoreUpdate(StoreBase):
    pass


class StoreCreate(StoreBase):
    name: str
    city: str
    country: str
    currency: constr(min_length=3, max_length=3)  # type: ignore
    zipcode: str
    street: str


class Store(StoreCreate):
    store_id: UUID4

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: Optional[str]
    price: Optional[condecimal(decimal_places=2)]  # type: ignore

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class ProductUpdate(ProductBase):
    pass


class ProductCreate(ProductBase):
    store_id: UUID4
    name: str
    price: condecimal(decimal_places=2)  # type: ignore


class Product(ProductCreate):
    product_id: UUID4

    class Config:
        orm_mode = True


class OrderItem(BaseModel):
    quantity: int = Field(..., gt=0)
    product: Product

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True


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


class OrderDetail(Order):
    order_id: UUID4
    date: datetime
    items: List[OrderItem]
