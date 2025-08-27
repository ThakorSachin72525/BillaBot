# utils.py
# This file will contain utility functions for file handling.

import pandas as pd

def read_excel_data(file_path):
    """
    Reads all data from the first sheet of an Excel file into a list of dictionaries.
    
    Args:
        file_path (str): The path to the Excel file.
        
    Returns:
        list: A list of dictionaries, where each dictionary represents a row.
              Returns an empty list if there's an error.
    """
    try:
        # pd.read_excel reads the data into a DataFrame.
        df = pd.read_excel(file_path)
        
        # We can drop any rows that have all NaN values (empty rows) to clean the data.
        df.dropna(how='all', inplace=True)
        
        # This is the key change. We use to_dict('records') to convert the DataFrame
        # directly into a list of dictionaries. Each dictionary's keys are the
        # column headers (e.g., 'SalesOrderID') and values are the row data.
        data = df.to_dict('records')
        return data
    except Exception as e:
        # If there's any issue reading the file, we print the error
        # and return an empty list.
        print(f"Error reading Excel file: {e}")
        return []

def save_dataframe_to_excel(df, file_path):
    """
    Saves a pandas DataFrame to an Excel file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_path (str): The path to the new Excel file.
    """
    try:
        # df.to_excel is a simple way to save the data.
        # We use index=False to prevent writing the row numbers to the file.
        df.to_excel(file_path, index=False)
    except Exception as e:
        print(f"Error saving DataFrame to Excel: {e}")

