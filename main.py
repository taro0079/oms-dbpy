import argparse
from CsvImporter import CsvImporter
from CsvRowReader import CsvRowReader
from DatabaseHandler import DataBaseHandler
from QueryCreator import QueryCreator


parser = argparse.ArgumentParser(prog="oms-dbpy", description="Import CSV to Database")
parser.add_argument("-c", "--csv", help="CSV filename", required=True)
parser.add_argument(
    "-t", "--table_name", help="table name you want to import", required=True
)
parser.add_argument(
    "-p", "--primary_key", help="primary key column name", required=True
)
args = parser.parse_args()
filename = args.csv
table_name = args.table_name
primary_key = args.primary_key
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
