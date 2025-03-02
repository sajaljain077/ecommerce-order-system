from fastapi import FastAPI
from app.api.v1.endpoints import orders, user
from app.core.queue import start_worker
from app.models import order_db
from app.db.database import engine

app = FastAPI()

@app.get('/', status_code=200)
def index_page():
    return {"message": f"App is running"}

@app.get('/ping', status_code=200)
def index_page():
    return {"message":"Success"}


# Include routers
app.include_router(orders.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")

# Create Schema in the DB
order_db.Base.metadata.create_all(engine)

# Start worker thread
start_worker()