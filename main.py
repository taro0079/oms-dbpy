from CsvImporter import CsvImporter
from CsvRowReader import CsvRowReader
from DatabaseHandler import DataBaseHandler
from QueryCreator import QueryCreator

filename = "test.csv"  # TODO: Change to argument
table_name = "mst_transfer_control"
primary_key = "id"


csvReader = CsvImporter(filename)
header = csvReader.get_header()
body = csvReader.get_body()
query_create = QueryCreator(table_name, header)
database = DataBaseHandler(
    host="localhost",
    user="app_user",
    port="3306",
    password="!ChangeMe!",
    database="app_db",
)
for r in body:
    csv_row_reader = CsvRowReader(header, r)
    primary_key_value = csv_row_reader.get_value(primary_key)
    select_query = query_create.select(primary_key, primary_key_value)
    target = database.select(select_query)
    if len(target) > 0:
        delete_query = query_create.delete(primary_key, primary_key_value)
        database.write(delete_query)
    database.write(query_create.create_insert_statement(r))
