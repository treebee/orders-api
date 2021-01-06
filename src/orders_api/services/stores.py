from fastapi import Depends
from sqlalchemy.orm import Session

from orders_api.db.models import Store
from orders_api.db.schemas import StoreCreate
from orders_api.db.session import get_session


class StoresService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def list(self):
        return self.db_session.query(Store).all()

    def get(self, store_id):
        return self.db_session.query(Store).get(store_id)

    def create(self, store: StoreCreate) -> Store:
        db_store = Store(**store.dict())
        self.db_session.add(db_store)
        self.db_session.commit()
        return db_store