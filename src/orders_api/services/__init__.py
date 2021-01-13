from fastapi import Depends
from sqlalchemy.orm import Session

from orders_api.db.session import get_session

from .orders import OrdersService
from .products import ProductsService
from .stores import StoresService


def get_stores_service(db_session: Session = Depends(get_session)) -> StoresService:
    return StoresService(db_session)


def get_products_service(db_session: Session = Depends(get_session)) -> ProductsService:
    return ProductsService(db_session)


def get_orders_service(db_session: Session = Depends(get_session)) -> OrdersService:
    return OrdersService(db_session)


__all__ = ("get_stores_service", "get_products_service", "get_orders_service")
