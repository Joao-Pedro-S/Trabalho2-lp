from produtoEstoque import ProdutoEstoque
class EstoqueProdutos():
    def __init__(self):
        self.produtos = {}

    def adicionaProduto(self, produto):
        self.produtos[produto.get_nome()] = produto

    def mostraEstoque(self):
        for obj in self.produtos:
            print(obj, ":", self.produtos[obj].get_quantidade())
