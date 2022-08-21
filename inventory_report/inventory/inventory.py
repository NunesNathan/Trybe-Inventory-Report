from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    def import_data(path, reportType):
        infos = list()
        report = str()

        if path.endswith(".csv"):
            infos = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            infos = JsonImporter.import_data(path)

        if reportType.lower() == "simples":
            report = SimpleReport.generate(infos)
        elif reportType.lower() == "completo":
            report = CompleteReport.generate(infos)

        return report
