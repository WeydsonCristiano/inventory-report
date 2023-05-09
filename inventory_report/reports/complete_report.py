from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(dados):
        data_fabricacao_mais_antiga = min(
            d["data_de_fabricacao"] for d in dados
        )
        data_validade_mais_proxima = max(d["data_de_validade"] for d in dados)

        empresas = [d["nome_da_empresa"] for d in dados]
        produtos = Counter(empresas)
        empresa_com_mais_produtos = produtos.most_common(1)[0][0]
        produtos_estocados = produtos.most_common(None)

        linhas_do_relatorio = [
            f"Data de fabricação mais antiga: {data_fabricacao_mais_antiga}\n",
            f"Data de validade mais próxima: {data_validade_mais_proxima}\n",
            f"Empresa com mais produtos: {empresa_com_mais_produtos}\n",
            "Produtos estocados por empresa:\n",
        ]
        for empresa, num_produtos in produtos_estocados:
            linhas_do_relatorio.append(f"- {empresa}: {num_produtos}\n")

        return "".join(linhas_do_relatorio)
