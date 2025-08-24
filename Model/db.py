from sqlalchemy import create_engine, text

server = "localhost"
database = "AdventureWorks2022"
username = "sa"   # your SQL login
password = "Admin123"

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(connection_string)

def clear_salesorderids():
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM ToolSalesOrderIDs"))