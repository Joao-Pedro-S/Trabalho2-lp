class ProdutoEstoque:
    #_nome: str
    #_valor: float
    #_quantidade: int

    def __init__(self, nome, valor, quantidade):
        self._nome = nome
        self._valor = valor
        self._quantidade = quantidade
        
    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome
    
    def get_valor(self):
        return self._valor
    
    def get_quantidade(self):
        return self._quantidade
    
    def reduzQuantia(self,quantidade):
        x = self.get_quantidade()
        x -= quantidade
        self.set_quantidade(x)

