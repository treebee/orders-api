from typing import Optional

from pydantic import BaseModel, HttpUrl
from pydantic.types import constr


class StoreCreate(BaseModel):
    name: str
    city: str
    country: str
    currency: constr(min_length=3, max_length=3)
    domain: Optional[HttpUrl]
    phone: Optional[str]
    zipcode: str


class Store(StoreCreate):
    store_id: int

    class Config:
        orm_mode = True
