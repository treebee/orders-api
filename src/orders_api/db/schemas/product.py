from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4, condecimal

from .utils import to_camel


class ProductBase(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True


class ProductUpdate(ProductBase):
    name: Optional[str]
    price: Optional[condecimal(decimal_places=2)]  # type: ignore


class ProductCreate(ProductBase):
    store_id: UUID4
    name: str
    price: condecimal(decimal_places=2)  # type: ignore


class Product(ProductCreate):
    product_id: UUID4

    class Config:
        orm_mode = True
