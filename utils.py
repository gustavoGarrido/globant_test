import psycopg2
import pandas as pd

def create_query(table_name:str, df_columns:list, env:str, index:int, df:pd.DataFrame):
    """
    It takes a table name, a list of columns, an environment, an index, and a dataframe, and returns a
    query string
    
    :param table_name: the name of the table you want to insert the data into
    :type table_name: str
    :param df_columns: list of columns in the dataframe
    :type df_columns: list
    :param env: the environment where the data will be inserted
    :type env: str
    :param index: the index of the row you want to create the query for
    :type index: int
    :param df: the dataframe that contains the data to be inserted
    :type df: pd.DataFrame
    :return: A query string
    """
    query_columns = f"insert into {env}_globant.{table_name}("
    query_values = 'values('
    contador = 0
    for column in df_columns:
        contador += 1
        value = df[column][index]
        if contador == len(df_columns):
            if value != 'NULL':
                query_columns = f"{query_columns} {column})"
                query_values = f"{query_values} '{value}')"
            else:
                query_columns = f"{query_columns[:-1]})"
                query_values = f"{query_values[:-1]})"
        else:
            if value != 'NULL':
                query_columns = f"{query_columns} {column},"
                query_values = f"{query_values} '{value}',"
    query = f"{query_columns} {query_values}"
    return query

def insert_data(df_columns:list, df:pd.DataFrame, conn, table_name:str, env:str):
    """
    It takes a list of columns, a dataframe, a connection, a table name and an environment and inserts
    the data into the table
    
    :param df_columns: list of columns in the dataframe
    :type df_columns: list
    :param df: the dataframe you want to insert
    :type df: pd.DataFrame
    :param conn: connection to the database
    :param table_name: the name of the table you want to insert data into
    :type table_name: str
    :param env: environment where the data is going to be inserted
    :type env: str
    :return: A dictionary with the status code and a message.
    """
    cursor = conn.cursor()
    try:
        for index in df.index:
            query = create_query(table_name=table_name,df_columns=df_columns,env=env,index=index, df=df)
            print(query)
            cursor.execute(query=query)
        conn.commit()
        conn.close()
        return {"statusCode":200, "message":"Datos insertados con exito"}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        conn.close()
        return {"statusCode": 500, "message":f"ha habido un error en la ejecucion en query {query}. Detalle del error: {error}"}
