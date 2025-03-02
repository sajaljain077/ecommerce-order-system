import time
from app.models.order_db import Order
from app.db.database import get_db
from fastapi.encoders import jsonable_encoder


def process_order(queue):
    """
    Worker function to process orders from the queue.
    """
    db = next(get_db())  # Get a database session
    while True:
        if queue.empty():
            time.sleep(10)
            continue
        order_data = jsonable_encoder(queue.get())
        if order_data is None:
            break
        try:
            # Fetch the order from the database
            order = db.query(Order).filter(Order.order_id == order_data["order_id"]).first()
            print("This is somethings")
            if not order:
                continue

            # Simulate processing time (5 seconds)
            time.sleep(5)
            order.status = "Processing"
            db.commit()

            # Simulate completion time (5 seconds)
            time.sleep(5)
            order.status = "Completed"
            db.commit()

        except Exception as e:
            db.rollback()
            print(f"Error processing order {order_data['order_id']}: {e}")
        finally:
            queue.task_done()