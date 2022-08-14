from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


def test_cria_produto():
    fake_product = ProductFactory()
    product = Product(
        fake_product.id,
        fake_product.nome_do_produto,
        fake_product.nome_da_empresa,
        fake_product.data_de_fabricacao,
        fake_product.data_de_validade,
        fake_product.numero_de_serie,
        fake_product.instrucoes_de_armazenamento)

    assert fake_product.id == product.id
    assert fake_product.nome_do_produto == product.nome_do_produto
    assert fake_product.nome_da_empresa == product.nome_da_empresa
    assert fake_product.data_de_fabricacao == product.data_de_fabricacao
    assert fake_product.data_de_validade == product.data_de_validade
    assert fake_product.numero_de_serie == product.numero_de_serie
    assert (
        fake_product
        .instrucoes_de_armazenamento == product.instrucoes_de_armazenamento)
