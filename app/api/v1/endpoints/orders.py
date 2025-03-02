from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.schemas.order import OrderCreate
from app.services.order_service import create_order, get_order_status, get_order_metrics
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter()

@router.post("/orders", tags=["Orders"])
async def create_order_endpoint(order: OrderCreate, db:Session=Depends(get_db)):
    return create_order(db, jsonable_encoder(order))


@router.get("/{user_id}/orders/{order_id}", tags=["Orders"])
async def get_order_status_endpoint(user_id:str, order_id: str, db:Session=Depends(get_db)):
    return get_order_status(db, user_id, order_id)


@router.get("/metrics", tags=["Orders"])
async def get_metrics(db:Session = Depends(get_db)):
    return get_order_metrics(db)
