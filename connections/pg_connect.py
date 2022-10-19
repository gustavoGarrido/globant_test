from ast import Return, Try
from ctypes.wintypes import PSHORT
import psycopg2
import os
import logging

def create_connection():
    HOST:str = os.environ.get("HOST")
    DATABASE:str = os.environ.get("DATABASE")
    USER:str = os.environ.get("USER")
    PASSWORD:str = os.environ.get("PASSWORD")
    PORT:str = os.environ.get("PORT")

    try:
        connection = psycopg2.connect(HOST=HOST, DATABASE=DATABASE,USER=USER,PASSWORD=PASSWORD,PORT=PORT)
        logging.info(f"service connected to database {DATABASE} en host {HOST} en port {PORT}")
        return connection
    except Exception as error:
        logging.error(f"there is a mistakes when the service try to connect. error details {error}")
        return error
    

    