from datetime import datetime
import time
from sqlalchemy.orm import Session
from app.models.order_db import Order
from app.schemas.order import OrderStatus
from fastapi import HTTPException
from app.db.database import get_db
from app.core.queue import order_queue

def create_order(db, order_data: dict):
    """
    Create a new order in the database and add it to the queue for processing.
    """
    order = Order(
        user_id=order_data["user_id"],
        item_ids=",".join(order_data["item_ids"]),
        total_amount=order_data["total_amount"],
        status="Pending"
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    order_queue.put(order)
    return order

def get_order_status(db, user_id:str, order_id: str):
    """
    Retrieve the status of an order by its ID.
    """
    order = db.query(Order).filter(Order.order_id == order_id, Order.user_id==user_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order