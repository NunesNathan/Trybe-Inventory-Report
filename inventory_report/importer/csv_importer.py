import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        with open(path) as file:
            return [row for row in csv.DictReader(
                file, delimiter=",", quotechar='"')]
