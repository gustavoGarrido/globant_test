from ast import Return, Try
from ctypes.wintypes import PSHORT
import psycopg2
import os
import logging

def create_connection():
    HOST:str = os.environ.get("PGHOST")
    DATABASE:str = os.environ.get("PGDATABASE")
    USER:str = os.environ.get("POSTGRES_USER")
    PASSWORD:str = os.environ.get("POSTGRES_PASSWORD")
    PORT:str = os.environ.get("PGPORT")

    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER,password=PASSWORD, port=PORT)
        logging.info(f"service connected to database {DATABASE} en host {HOST} en port {PORT}")
        print(f"service connected to database {DATABASE} en host {HOST} en port {PORT}")
        return connection
    except Exception as error:
        logging.error(f"there is a mistakes when the service try to connect. error details {error}")
        print(f"there is a mistakes when the service try to connect. error details {error}")
        return error
    

    