from sqlalchemy import Column, String, Float, DateTime, Enum, ForeignKey, Integer
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(50), ForeignKey("users.user_id"), nullable=False)
    item_ids = Column(String(255), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum("Pending", "Processing", "Completed"), default="Pending")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    user = relationship("User", back_populates="orders")

class User(Base):
    __tablename__ = "users"
    user_id = Column(String(50), primary_key=True) 
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    orders = relationship("Order", back_populates="user")