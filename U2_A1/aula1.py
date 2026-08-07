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
