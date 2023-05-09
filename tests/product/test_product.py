from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        id=1,
        nome_da_empresa="Target Corporation",
        nome_do_produto="Nicotine Polacrilex",
        data_de_fabricacao="2021-02-18",
        data_de_validade="2023-09-17",
        numero_de_serie="CR25 1551 4467 2549 4402 1",
        instrucoes_de_armazenamento="instrucao 1",
    )
    assert produto.id == 1
    assert produto.nome_da_empresa == "Target Corporation"
    assert produto.nome_do_produto == "Nicotine Polacrilex"
    assert produto.data_de_fabricacao == "2021-02-18"
    assert produto.data_de_validade == "2023-09-17"
    assert produto.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert produto.instrucoes_de_armazenamento == "instrucao 1"
