import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:

    @staticmethod
    def import_data(path, reportType):
        with open(path) as file:
            infos = [row for row in csv.DictReader(
                file, delimiter=",", quotechar='"')]

            report = str()
            if reportType == "simples":
                report = SimpleReport.generate(infos)
            elif reportType == "completo":
                report = CompleteReport.generate(infos)

        return report
