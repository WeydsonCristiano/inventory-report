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
        estoq_products = products.most_common(None)

        report_lines = [
            f"Data de fabricação mais antiga: {min_date}\n",
            f"Data de validade mais próxima: {max_date}\n",
            f"Empresa com mais produtos: {max_products}\n",
            "Produtos estocados por empresa:\n",
        ]
        for empresa, num_products in estoq_products:
            report_lines.append(f"- {empresa}: {num_products}\n")

        return "".join(report_lines)
