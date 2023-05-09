from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        id=1,
        nome_do_produto="Farinha",
        nome_da_empresa="Farinini",
        data_de_fabricacao="2021-05-01",
        data_de_validade="2023-06-02",
        numero_de_serie="fr48",
        instrucoes_de_armazenamento="ao abrigo de luz",
    )

    assert str(produto) == (
        "O produto Farinha fabricado em 2021-05-01 por "
        + "Farinini com validade até 2023-06-02 precisa "
        + "ser armazenado ao abrigo de luz."
    )
