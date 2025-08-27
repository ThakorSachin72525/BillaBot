from Model.db import db
from Model.service import clear_salesorderids, get_salesorderids, insert_salesorderid, get_initial_id_count

def clear_table():
    clear_salesorderids()

def get_ids_count():
    return get_initial_id_count()
    