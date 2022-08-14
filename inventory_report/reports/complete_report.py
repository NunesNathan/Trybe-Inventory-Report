from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def company_items(list):
        companies = dict()

        for product in list:
            company = product['nome_da_empresa']
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1

        items = str()

        for (company, quantity) in companies.items():
            items += f"- {company}: {quantity}\n"

        return items

    @staticmethod
    def generate(list):
        simple = SimpleReport.generate(list)

        return f"""{simple}\nProdutos estocados por empresa:
{CompleteReport.company_items(list)}"""
