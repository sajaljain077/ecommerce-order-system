from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from app.schemas.user import UserCreate
from app.services.user_service import create_user
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.post("/user", status_code=201, tags=["User"])
async def create_user_endpoint(user_payload: UserCreate, db:Session=Depends(get_db)):
    return create_user(db, jsonable_encoder(user_payload))

