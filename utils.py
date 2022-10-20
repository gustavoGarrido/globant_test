import psycopg2
import pandas as pd

def create_query(table_name:str, df_columns:list, env:str, index:int, df:pd.DataFrame):
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