import datetime as dt
from statistics import mode

# datetime module
# https://youtu.be/r1Iv4d6CO2Q?list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn

# statistics module
# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/


class SimpleReport:
    @staticmethod
    def _get_dates(products, where):
        dates = [
          dt.datetime.strptime(
            product[where], "%Y-%m-%d") for product in products
        ]

        return min(dates)

    @staticmethod
    def _most_viewed_company(products):
        names = [
          product["nome_da_empresa"] for product in products
        ]

        return mode(names)

    @staticmethod
    def generate(list):
        return (
          "Data de fabricação mais antiga: "
          f"{SimpleReport._get_dates(list, 'data_de_fabricacao').date()}"
          "\nData de validade mais próxima: "
          f"{SimpleReport._get_dates(list, 'data_de_validade').date()}"
          f"\nEmpresa com mais produtos: "
          f"{SimpleReport._most_viewed_company(list)}")
