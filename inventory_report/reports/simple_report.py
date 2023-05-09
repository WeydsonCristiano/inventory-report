from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        oldest_date = min(
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
            for product in products
        ).strftime("%Y-%m-%d")

        closest_validity = min(
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            for product in products
            if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ).strftime("%Y-%m-%d")

        companies = {}
        for product in products:
            company_name = product["nome_da_empresa"]
            if company_name in companies:
                companies[company_name] += 1
            else:
                companies[company_name] = 1

        most_products_company = max(companies, key=companies.get)

        report = f"Data de fabricação mais antiga: {oldest_date}\n"
        report += f"Data de validade mais próxima: {closest_validity}\n"
        report += f"Empresa com mais produtos: {most_products_company}"

        return report
