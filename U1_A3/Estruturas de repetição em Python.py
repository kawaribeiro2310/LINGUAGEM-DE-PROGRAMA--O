
numero = int(input("Digite um número: "))

while numero != 0:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar") 
        break

    for i in range(1, 11):
        print(i)
