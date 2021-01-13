from fastapi import HTTPException
from sqlalchemy.orm import Session

from orders_api.db.models import Product, Store
from orders_api.db.schemas import ProductCreate, ProductUpdate

from .base import BaseService


class ProductsService(BaseService[Product, ProductCreate, ProductUpdate]):
    def __init__(self, db_session: Session):
        super(ProductsService, self).__init__(Product, db_session)

    def create(self, obj: ProductCreate) -> Product:
        store = self.db_session.query(Store).get(obj.store_id)
        if store is None:
            raise HTTPException(
                status_code=400,
                detail=f"Store with storeId = {obj.store_id} not found.",
            )
        return super(ProductsService, self).create(obj)
