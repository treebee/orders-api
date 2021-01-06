from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True)
    name = Column(Text)
    city = Column(Text)
    country = Column(Text)
    currency = Column(String(3))
    domain = Column(Text)
    street = Column(Text)
    zipcode = Column(Text)
    phone = Column(Text)
