import csv


class CsvImporter:
    def __init__(self, filename: str, delimiter: str = "\t"):
        self.filename = filename
        self.delimiter = delimiter

    def read(self):
        with open(self.filename, encoding="utf8") as f:
            reader = csv.reader(f, delimiter=self.delimiter)
            result = [row for row in reader]
        return result

    def getHeder(self):
        return self.read()[0]

    def getBody(self):
        return self.read()[1:]
