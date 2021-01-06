from fastapi import Depends
from sqlalchemy.orm import Session

from orders_api.db.session import get_session
from .stores import StoresService


def get_stores_service(db_session: Session = Depends(get_session)):
    return StoresService(db_session)