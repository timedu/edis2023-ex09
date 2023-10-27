
import requests # pyright: ignore
from os import environ 


def post_request(node_id, data):

    url = f'http://dbms{node_id}:4000'
    response = requests.post(url, json = data)
    return response.json() 


def get_client_id():

    return environ.get('HOSTNAME','??????????')[9:]

