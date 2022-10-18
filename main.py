import datetime
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
import pandas as pd


app = FastAPI()

class Request(BaseModel):
    database: str = Field(description="name of database that allocated the data")
    schema_name:str = Field(description="name of schema that allocated the data")
    table_name: str = Field(description="name of table that allocated the data")
    data:list = Field(description="data will be allocated")

@app.post("/load_data")
def read_root(request:Request):

    data_to_database = request.data

    if len(data_to_database) > 1000:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="only can process 1000 or less") 
 
    df = pd.DataFrame.from_records(data_to_database)
    print(df)
    return request.data
