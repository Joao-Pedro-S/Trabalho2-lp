from produtoEstoque import ProdutoEstoque
class CarrinhoCompra():
    def __init__(self, estoque):
        self.estoque = estoque
        self.compras = {}

    def adicionaItem(self, produto, quant):
        if self.estoque.produtos.get(produto):
            self.compras[produto] = quant #nome do produto é usado como chave, quant é valor.

    def calculaTotal(self):
        #total: float
        total = 0
        for item in self.compras:
            total += self.estoque.produtos[item].get_valor() * self.compras[item]
        return total
    
    def finalizaCompra(self):
        for item in self.compras:
            a = self.compras[item]
            #print(a)
            self.estoque.produtos[item].reduzQuantia(a)
            #self.estoque.produtos[item]