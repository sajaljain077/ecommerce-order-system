from sqlalchemy.orm import Session
from app.models.order_db import Order
from app.schemas.order import OrderCreate, OrderStatus

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, order: OrderCreate):
        """
        Create a new order in the database.
        """
        db_order = Order(
            order_id=order.order_id,
            user_id=order.user_id,
            item_ids=",".join(order.item_ids),
            total_amount=order.total_amount,
            status="Pending"
        )
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_order_by_id(self, order_id: str):
        """
        Retrieve an order by its ID.
        """
        return self.db.query(Order).filter(Order.order_id == order_id).first()

    def update_order_status(self, order_id: str, status: str):
        """
        Update the status of an order.
        """
        db_order = self.get_order_by_id(order_id)
        if db_order:
            db_order.status = status
            self.db.commit()
            self.db.refresh(db_order)
        return db_order

    def get_all_orders(self):
        """
        Retrieve all orders from the database.
        """
        return self.db.query(Order).all()

    def get_orders_by_status(self, status: str):
        """
        Retrieve orders by their status.
        """
        return self.db.query(Order).filter(Order.status == status).all()