class CsvRowReader:
    def __init__(self, columns: list[str], row: list[str]) -> None:
        self.columns = columns
        self.row = row

    def _get_index(self, primary_key_column_name: str):
        if primary_key_column_name not in self.columns:
            raise ValueError(f"{primary_key_column_name} is not in header")
        return self.columns.index(primary_key_column_name)

    def get_value(self, primary_key_column_name: str):
        return self.row[self._get_index(primary_key_column_name)]
