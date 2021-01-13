from sqlalchemy.orm import Session

from orders_api.db.models import Store
from orders_api.db.schemas import StoreCreate, StoreUpdate

from .base import BaseService


class StoresService(BaseService[Store, StoreCreate, StoreUpdate]):
    def __init__(self, db_session: Session):
        super(StoresService, self).__init__(Store, db_session)
