Nota_1 = int(input('Digite a primeira nota: '))
Nota_2 = int(input('Digite a segunda nota: '))
Nota_3 = int(input('Digite a terceira nota: '))
Nota_4 = int(input('Digite a quarta nota: '))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4
print(f"A média das notas é: {media}")

Aprovado = media >= 7
if Aprovado:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")