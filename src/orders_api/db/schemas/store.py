from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl
from pydantic.types import UUID4, constr

from .utils import to_camel


class StoreBase(BaseModel):
    name: Optional[str]
    city: Optional[str]
    country: Optional[str]
    currency: Optional[constr(min_length=3, max_length=3)]  # type: ignore
    domain: Optional[HttpUrl]
    phone: Optional[str]
    street: Optional[str]
    zipcode: Optional[str]
    email: Optional[EmailStr]


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
        alias_generator = to_camel
        allow_population_by_field_name = True
