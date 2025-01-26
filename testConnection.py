# test_connection.py
from app.db.database import engine
from app.db.models import Base

def test_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Database connection successful")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_db()