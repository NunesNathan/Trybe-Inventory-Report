import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        with open(path) as file:
            return [row for row in json.load(file)]
