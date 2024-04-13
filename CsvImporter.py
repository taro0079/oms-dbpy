import csv


class CsvImporter:
    def __init__(self, filename: str, delimiter: str = "\t"):
        self.filename = filename
        self.delimiter = delimiter
        self.read_flag = False
        self.read_data = []

    def read(self):
        with open(self.filename, encoding="utf8") as f:
            reader = csv.reader(f, delimiter=self.delimiter)
            result = [row for row in reader]
        self.read_flag = True
        self.read_data = result
        return result

    def get_header(self):
        if not self.read_flag:
            return self.read()[0]
        return self.read_data[0]

    def get_body(self):
        if not self.read_flag:
            return self.read()[1:]
        return self.read_data[1:]

    def get_index_column(self, column_name: str):
        header = self.get_header()
        if column_name not in header:
            raise ValueError(f"{column_name} is not in header")
        return header.index(column_name)
