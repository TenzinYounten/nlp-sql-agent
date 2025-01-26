# test_db.py
from app.db.database import engine

with engine.connect() as conn:
    result = conn.execute("SELECT * from orders")
    print("DB Connected")