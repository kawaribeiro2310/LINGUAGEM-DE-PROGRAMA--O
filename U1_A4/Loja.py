def calcular_desconto(preco, percentual):
    """
    Calcula o valor do desconto com base no preço e no percentual fornecido.

    Args:
        preco (float): O preço original do produto.
        percentual (float): O percentual de desconto a ser aplicado.

    Returns:
        float: O valor do desconto calculado.
    """
    if percentual < 0 or percentual > 100:
        return None  # Retorna None se o percentual for inválido
    desconto = preco * (percentual / 100)
    return preco - desconto

def registrar_venda(produto, preco, percentual_desconto):
    """
    Registra uma venda de produto, calculando o preço final após o desconto.

    Args:
        produto (str): O nome do produto.
        preco (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado.

    Returns:
        float: O preço final do produto após o desconto.
    """
    preco_final = calcular_desconto(preco, percentual_desconto)
    return preco_final

print("Bem-vindo à loja!")
produto = input("Digite o nome do produto: ")  
preco = float(input("Digite o preço do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto (0 a 100): "))
preco_final = registrar_venda(produto, preco, percentual_desconto)
print(f"O preço final do produto '{produto}' é: R$ {preco_final:.2f}")

#Loop para permitir que o usuário registre várias vendas
while True:
    continuar = input("Deseja registrar outra venda? (s/n): ").lower()
    if continuar == 's':
        produto = input("Digite o nome do produto: ")  
        preco = float(input("Digite o preço do produto: "))
        percentual_desconto = float(input("Digite o percentual de desconto (0 a 100): "))
        preco_final = registrar_venda(produto, preco, percentual_desconto)
        print(f"O preço final do produto '{produto}' é: R$ {preco_final:.2f}")
    elif continuar == 'n':
        print("Obrigado por utilizar a loja!")
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")