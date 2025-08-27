from Model.db import db

def clear_salesorderids():
    """Delete all sales order IDs"""
    db.execute_query("DELETE FROM ToolSalesOrderIDs")

def get_salesorderids():
    """Fetch all sales order IDs"""
    return db.fetch_all("SELECT * FROM ToolSalesOrderIDs")

def insert_salesorderid(order_id):
    """Insert one sales order ID"""
    db.execute_query(
        "INSERT INTO ToolSalesOrderIDs (SalesOrderID) VALUES (:id)",
        {"id": order_id}
    )

def get_initial_id_count():
    """Get the count of IDs in the ToolSalesOrderIDs table"""
    result = db.fetch_one("SELECT COUNT(SalesOrderID) AS count FROM ToolSalesOrderIDs")
    return result[0]

def insert_salesorderids(data):
    """
    Insert a list of records (dictionaries) into the ToolSalesOrderIDs table.
    This is a bulk insert for efficiency.
    
    Args:
        data (list of dict): A list where each dictionary represents a row
                            with keys matching the database column names.
    """
    # The `data` parameter is expected to be a list of dictionaries,
    # for example: [{'SalesOrderID': 123}, {'SalesOrderID': 456}].
    # SQLAlchemy's `execute` method can handle this format for a bulk insert.
    db.execute_query(
        "INSERT INTO ToolSalesOrderIDs (SalesOrderID) VALUES (:SalesOrderID)",
        data
    )