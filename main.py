from CsvImporter import CsvImporter
from DatabaseHandler import DataBaseHandler
from QueryCreator import QueryCreator

filename = "test.csv"  # TODO: Change to argument

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

select_query = query_create.select("id", "1")
target = database.select(select_query)
if len(target) > 0:
    delete_query = query_create.delete("id", "1")
    database.write(delete_query)
database.write(query_create.create_insert_statement(body[0]))
