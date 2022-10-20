import os
from typing import Any
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
from connections.pg_connect import create_connection 
import psycopg2
from utils import insert_data


app = FastAPI()


class Request(BaseModel):
    table_name: str = Field(description="name of table that allocated the data")
    data:list = Field(description="data will be allocated")

ENV:str = os.environ.get("enviroment")

@app.post("/load_data")
def read_root(request:Request):

    table_name:str = request.table_name
    data_to_insert = request.data

    df = pd.DataFrame.from_records(data_to_insert)
    df.fillna('NULL', inplace=True)
    df_columns:list = df.columns.values

    if len(data_to_insert) > 1000:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="only can process 1000 or less") 
    
    connection = create_connection()

    insert_records=insert_data(df_columns=df_columns
                                ,df=df
                                ,conn=connection
                                ,table_name=table_name
                                ,env=ENV)

    if insert_records["statusCode"] == 200:
        return insert_records['message']
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=insert_records['message']) 
        

