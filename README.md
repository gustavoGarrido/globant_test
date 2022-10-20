# BUILD AND UP
docker-compose buid
docker-compose up

# USAGE IN DEV ENVIROMENT

open the url localhost:80/docs
send a request indicating the table name and data to insert
the request must to have the following structure

{
    table_mane:str,
    data:list[dict]
}