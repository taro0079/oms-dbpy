from CsvImporter import CsvImporter
from DatabaseHandler import DataBaseHandler
from QueryCreator import QueryCreator

filename = "test.csv"

csvReader = CsvImporter(filename)
header = csvReader.getHeder()
body = csvReader.getBody()
query_create = QueryCreator("mst_transfer_control", header)
database = DataBaseHandler(
    host="localhost",
    user="app_user",
    port="3306",
    password="!ChangeMe!",
    database="app_db",
)
# print(query_create.create_insert_statement(body[0]))
database.write(query_create.create_insert_statement(body[0]))
