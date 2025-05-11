import time
import psycopg2
from fastapi import FastAPI
from .connection import models
from .connection.database import engine, DATABASE_URL
from .router import router_manager

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(DATABASE_URL)
            cursor = conn.cursor()
            print(f"Database is connected")
            break
        except Exception as e:
            print(f"Error connecting to database: {e}")
            time.sleep(15)

"""@app.get("/")
def root():
    try:
        conn = connect_to_db()
        conn.cursor.execute("SELECT * FROM test_table")
        rows = connect_to_db.cursor.fetchall()
        return {"data": rows}
    except Exception as e:
        return {"error": str(e)}"""

app.include_router(router_manager.routerManager)