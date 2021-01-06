from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from orders_api.config import get_settings


engine = create_engine(get_settings().database_url, pool_pre_ping=True)


@lru_cache
def create_session():
    Session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return Session


def get_session() -> Session:
    db_session = create_session()
    try:
        yield db_session
    finally:
        db_session.remove()