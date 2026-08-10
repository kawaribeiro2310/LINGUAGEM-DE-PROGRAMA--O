class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

def comprimentar(self):
    return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

def aniversario(self):
    self.idade += 1
    return f"Feliz aniversário, {self.nome}! Agora você tem {self.idade} anos."

pessoa1 = Pessoa("João", 25)
print(pessoa1.comprimentar())  # Saída: Olá, meu nome é João e tenho 25 anos.
print(pessoa1.aniversario())  # Saída: Feliz aniversário, João! Agora você tem 26 anos. 