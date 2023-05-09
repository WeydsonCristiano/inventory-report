from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(dados):
        simplArmaz = SimpleReport.generate(dados)
        empresas = [d["nome_da_empresa"] for d in dados]
        produtos = Counter(empresas)

        produtos_estocados = produtos.most_common(None)
        linhas_do_relatorio = (
            simplArmaz + "\nProdutos estocados por empresa:\n"
        )

        for empresa, num_produtos in produtos_estocados:
            linhas_do_relatorio += f"- {empresa}: {num_produtos}\n"

        return "".join(linhas_do_relatorio)
