from estoqueProdutos import EstoqueProdutos
from carrinhoCompra import CarrinhoCompra
from produtoEstoque import ProdutoEstoque



estoque = EstoqueProdutos()
estoque.adicionaProduto(ProdutoEstoque("monitor", 500, 100))
estoque.adicionaProduto(ProdutoEstoque("telefone", 150, 300))
estoque.adicionaProduto(ProdutoEstoque("teclado", 70, 50))
estoque.adicionaProduto(ProdutoEstoque("mouse", 50, 50))


carrinho = CarrinhoCompra(estoque)
carrinho.adicionaItem("monitor", 2)
carrinho.adicionaItem("telefone", 5)
carrinho.adicionaItem("teclado", 2)
carrinho.adicionaItem("mouse", 4)

for obj in carrinho.compras:
    print(obj, ":", carrinho.compras[obj])


carrinho.finalizaCompra()

print("Sobra no estoque:")
estoque.mostraEstoque()

print("A soma dos produtos  :", carrinho.calculaTotal())