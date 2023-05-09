from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(produtos):
        data_fabricacao_mais_antiga = min(
            datetime.strptime(produto["data_de_fabricacao"], "%Y-%m-%d")
            for produto in produtos
        ).strftime("%Y-%m-%d")

        validade_mais_proxima = min(
            datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            for produto in produtos
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ).strftime("%Y-%m-%d")

        empresas = {}
        for produto in produtos:
            nome_da_empresa = produto["nome_da_empresa"]
            if nome_da_empresa in empresas:
                empresas[nome_da_empresa] += 1
            else:
                empresas[nome_da_empresa] = 1

        empresa_com_mais_produtos = max(empresas, key=empresas.get)

        relatorio = (
            f"Data de fabricação mais antiga: {data_fabricacao_mais_antiga}\n"
        )
        relatorio += (
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
        )
        relatorio += f"Empresa com mais produtos: {empresa_com_mais_produtos}"

        return relatorio
