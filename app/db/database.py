from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time


DESIRED_RETRY_COUNT = 5
re_try_count = 0

# sqlalchemyDatabaseUrl = engine + '://' + user_name + ':' + password + '@' + host + '/' + targated_schema_into_db
sqlalchemyDatabaseUrl = 'mysql+pymysql://root:root@localhost:3306/order_db'

while True:
    re_try_count = re_try_count + 1
    try:
        engine = create_engine(sqlalchemyDatabaseUrl, pool_pre_ping=True)
        print("database connection is successful")
        break
    except Exception as err:
        time.sleep(5)
    if re_try_count == DESIRED_RETRY_COUNT:
        raise Exception(f"Not able to connect to DB instance {err}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
