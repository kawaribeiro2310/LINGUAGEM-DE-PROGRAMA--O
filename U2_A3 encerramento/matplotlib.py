import matplotlib.pyplot as plt


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} - Preço: R$ {self.preco:.2f} - Quantidade: {self.quantidade}"

#Catalogo

catalogo = []
produto1 = Produto("Produto 1", 10.0, 5)

def adicionar_produto(nome, preco, quantidade):
    produto = Produto(nome, preco, quantidade)
    catalogo.append(produto)
    print(f"Produto '{nome}' adicionado ao catálogo.")

#Cadastrando produtos
adicionar_produto("Produto 1", 10.0, 5)
adicionar_produto("Produto 2", 20.0, 3)

lista_produtos = [str(produto) for produto in catalogo]

print("Catálogo de Produtos:")
for produto in lista_produtos:
    print(produto)

print("Bem-vindo à loja!")
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (0 a 100): "))
preco_final = U1_A4.Loja.registrar_venda(produto, preco, percentual_desconto)
print(f"O preço final do produto '{produto}' é: R$ {preco_final:.2f}")
print("Deseja registrar outra venda? (s/n): ")
resposta = input().lower()
if resposta == "s":
    pass
else:
    print("Obrigado por utilizar a loja!")