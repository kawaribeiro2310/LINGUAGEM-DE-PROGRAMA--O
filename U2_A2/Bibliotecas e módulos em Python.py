# Primeira forma de importar uma biblioteca
import math
print("Raiz quadrada de 16:", math.sqrt(16))
print("Valor de pi:", math.pi)
print("Fatorial de 5:", math.factorial(5))

# Segunda forma de importar uma biblioteca

import math as m
print("Raiz quadrada de 25:", m.sqrt(25))
print("Valor de pi:", m.pi)
print("Fatorial de 5:", m.factorial(5))

#Terceira forma de importar uma biblioteca
from math import sqrt, pi, factorial

print("Raiz quadrada de 36:", sqrt(36))
print("Valor de pi:", pi)
print("Fatorial de 6:", factorial(6))