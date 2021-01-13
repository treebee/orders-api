from typing import Any

from sqlalchemy.orm import Session

from orders_api.db.models import Order, OrderItem
from orders_api.db.schemas import OrderCreate

from .base import BaseService


class OrdersService(BaseService[Order, OrderCreate, Any]):
    def __init__(self, db_session: Session):
        super(OrdersService, self).__init__(Order, db_session)

    def create(self, obj: OrderCreate) -> Order:
        order = Order()
        self.db_session.add(order)
        self.db_session.flush()
        order_items = [
            OrderItem(**item.dict(), order_id=order.order_id) for item in obj.items
        ]
        self.db_session.add_all(order_items)
        self.db_session.commit()
        return order
