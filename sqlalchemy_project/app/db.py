from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:meelloo@localhost:5432/training_db"

engine = create_engine(DATABASE_URL, echo=True)
