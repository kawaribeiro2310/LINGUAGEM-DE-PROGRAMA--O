import matplotlib.pyplot as plt
def init(self,nome,preco,quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

    def __str__(self):
        return (f{self.nome} - Preço: R$ {self.preco:.2f} - Quantidade: {self.quantidade}")