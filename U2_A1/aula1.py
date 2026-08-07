import sys
from abc import ABC, abstractmethod

texto = "Explorando a diversidade de liguagens de programação, cada uma com suas características únicas e aplicações específicas. Python, por exemplo, é conhecida por sua sintaxe clara e legibilidade, tornando-a ideal para iniciantes e para desenvolvimento rápido de protótipos. Java, por outro lado, é amplamente utilizada em aplicações corporativas devido à sua robustez e portabilidade. C++ oferece controle detalhado sobre recursos de hardware, sendo preferida em sistemas que exigem alto desempenho. JavaScript domina o desenvolvimento web, permitindo a criação de interfaces interativas e dinâmicas. Cada linguagem tem seu lugar no ecossistema de desenvolvimento, e a escolha depende das necessidades do projeto e das habilidades da equipe envolvida."

print(tamanho_texto := len(texto))
tambem_possui_a = "a" in texto
print(f"O texto possui {tamanho_texto} caracteres.")
print(f"O texto possui a letra 'a': {tambem_possui_a}")
print(f"As 5 primeiras letras do texto são: {texto[:5]}")

cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
print(f"As cores disponíveis são: {', '.join(cores)}")
print(f"A primeira cor da lista é: {cores[0]}")
if "laranja" not in cores:
    print("A cor laranja não está na lista de cores disponíveis.")
else:
    print("A cor laranja está na lista de cores disponíveis.")
cor_escolhida = input("escolha uma cor da lista acima: ")
print(f"A cor escolhida foi: {cor_escolhida}")
print(f"A cor escolhida está na lista de cores disponíveis: {cor_escolhida in cores}")

class print(ABC):
    """Interface para tipos de saída de texto."""

    @abstractmethod
    def write(self, message: str) -> int:
        """Escreve texto em um fluxo de saída."""
        raise NotImplementedError

    @abstractmethod
    def write_line(self, message: str) -> int:
        """Escreve texto em uma linha do fluxo de saída."""
        raise NotImplementedError


class ConsolePrint(print):
    """Implementação concreta útil para uma classe de impressão."""

    def __init__(self, stream=None):
        self.stream = stream or sys.stdout

    def write(self, message: str) -> int:
        rendered = str(message)
        self.stream.write(rendered)
        return len(rendered)

    def write_line(self, message: str) -> int:
        rendered = str(message)
        self.stream.write(rendered + "\n")
        return len(rendered) + 1


printer = ConsolePrint()
printer.write_line("Saída criada pelo ConsolePrint.")