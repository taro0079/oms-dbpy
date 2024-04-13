class QueryCreator:

    def __init__(self, table_name: str, columns: list[str]) -> None:
        self.table_name = table_name
        self.columns = columns

    def create_insert_statement(self, row: list[str]):
        apply_column = f"INSERT INTO {self.table_name} ({', '.join(self.columns)}) VALUES ({', '.join(['%s' for _ in self.columns])})"
        quote_value = ["'" + value + "'" for value in row]
        return apply_column % tuple(quote_value)

    def select(self, primary_key: str, value: str):
        return f"SELECT * FROM {self.table_name} WHERE {primary_key} = {value}"

    def delete(self, primary_key: str, value: str):
        return f"DELETE FROM {self.table_name} WHERE {primary_key} = {value}"
