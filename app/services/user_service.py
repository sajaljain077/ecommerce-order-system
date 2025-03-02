from datetime import datetime
import time
from sqlalchemy.orm import Session
from app.models.order_db import User
from app.schemas.order import OrderStatus
from fastapi import HTTPException
import uuid

def create_user(db, user_data: dict):
    """
    Create a new order in the database and add it to the queue for processing.
    """
    user = db.query(User).filter(User.email == user_data.get("email")).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists with given email")
    user = User(
        user_id=uuid.uuid4(),
        name=user_data.get("name"),
        email=user_data.get("email"),
        password=user_data.get("password"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user