from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    user_id: str
    item_ids: List[str]
    total_amount: float

class OrderStatus(BaseModel):
    order_id: str
    status: str