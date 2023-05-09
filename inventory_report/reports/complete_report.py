from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        min_date = min(d["data_de_fabricacao"] for d in data)
        max_date = max(d["data_de_validade"] for d in data)

        empresas = [d["nome_da_empresa"] for d in data]
        products = Counter(empresas)
        max_products = products.most_common(1)[0][0]
        sorted_company_products = products.most_common(None)

        report_lines = [
            f"Data de fabricação mais antiga: {min_date}",
            f"Data de validade mais próxima: {max_date}",
            f"Empresa com mais produtos: {max_products}",
            "Produtos estocados por empresa:",
        ]
        for empresa, num_products in sorted_company_products:
            report_lines.append(f"- {empresa}: {num_products}")

        return "\n".join(report_lines)
