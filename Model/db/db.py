import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
driver = os.getenv("DB_DRIVER")

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)

engine = create_engine(connection_string)

def execute_query(sql, params=None):
    """Execute INSERT, UPDATE, DELETE"""
    with engine.begin() as conn:
        conn.execute(text(sql), params or {})

def fetch_all(sql, params=None):
    """Execute SELECT and return all rows"""
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        return result.fetchall()

def fetch_one(sql, params=None):
    """Execute SELECT and return one row"""
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        return result.fetchone()

