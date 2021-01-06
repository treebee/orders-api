from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

from orders_api.app import create_app
from orders_api.db.models import Base
from orders_api.db.session import create_session


@pytest.fixture(scope="session")
def db() -> Session:
    db_session = create_session()
    engine = db_session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all()
    Base.metadata.create_all()
    yield db_session


@pytest.fixture()
def app_client(db) -> Generator:
    # clean up tables before each test
    for table in Base.metadata.sorted_tables:
        db.execute(table.delete())
    app = create_app()
    yield TestClient(app)
