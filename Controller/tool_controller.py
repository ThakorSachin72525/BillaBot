from Model.utils import read_excel_data, save_dataframe_to_excel
from Model.service import (
    clear_salesorderids, 
    get_initial_id_count,
    insert_salesorderids
)
def clear_table():
    clear_salesorderids()
    new_count = get_initial_id_count()
    return new_count

def get_ids_count():
    return get_initial_id_count()

def handle_upload_ids(file_path):
    """
    This new function reads IDs from an Excel file, clears the table,
    and inserts the new IDs into the database.
    
    Args:
        file_path (str): The path to the Excel file to upload.
        
    Returns:
        tuple: A tuple containing the number of IDs uploaded and the new total count.
    """
    # Read the IDs from the Excel file using your utility function.
    ids = read_excel_data(file_path)
    
    # Now, insert all the new IDs at once. We'll need to create this function.
    insert_salesorderids(ids)
    
    uploaded_count = len(ids)
    total_count = get_initial_id_count()
    
    return uploaded_count, total_count


    