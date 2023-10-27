
from datetime import datetime
from os import environ 


def get_date_string():
    return datetime.now().strftime('%c')

def get_node_id():
    return environ.get('NODE_ID', '?')
