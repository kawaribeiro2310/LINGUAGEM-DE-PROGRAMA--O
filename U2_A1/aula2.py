meu_conjuto = set()  # Cria um conjunto vazio
meu_conjuto.add(1)  # Adiciona o elemento 1 ao  conjunto   
meu_conjuto.add(2)  # Adiciona o elemento 2 ao conjunto
meu_conjuto.add(3)  # Adiciona o elemento 3 ao conjunto
meu_conjuto.remove(2)  # Remove o elemento 2 do conjunto
meu_conjuto
{1, 2, 3}

elemento = 2
if elemento in meu_conjuto:
    print(f"O elemento {elemento} está presente no conjunto.")
else:
    print(f"O elemento {elemento} não está presente no conjunto.")

numeros_com_repetiçoes = [1, 2, 3, 2, 4, 1, 5]

unicos = set(numeros_com_repetiçoes)  # Converte a lista em um conjunto para remover duplicatas
print(unicos)  # Saída: {1, 2, 3, 4, 5}