from app.models.order_db import Order, User
from sqlalchemy import func, text
from app.schemas.order import OrderStatus
from fastapi import HTTPException
from app.db.database import get_db
from app.core.queue import order_queue

def create_order(db, order_data: dict):
    """
    Create a new order in the database and add it to the queue for processing.
    """
    user = db.query(User).filter(User.email == order_data["user_email"]).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    order = Order(
        user_id=user.user_id,
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

def get_order_metrics(db):
    """
    Retrieve metrics for orders in the database.
    """ 
    # Total number of orders
    total_orders = db.query(func.count(Order.order_id)).scalar()

    # Average processing time for completed orders
    avg_processing_time = db.query(
        func.avg(Order.completion_time)
    ).filter(Order.status == 'Completed').scalar()

    # Count of orders in each status
    status_counts = db.query(
        Order.status,
        func.count(Order.order_id)
    ).group_by(Order.status).all()

    return {
        "total_orders": total_orders,
        "avg_processing_time": avg_processing_time,
        "status_counts": dict(status_counts)
    }