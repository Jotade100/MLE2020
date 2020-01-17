import math as math

def sacar_factores(numero):
    for i in range(math.floor(math.sqrt(numero)), 2, -1):
        if numero % i == 0:
            if es_primo(i):
                return i


def es_primo(factor):
    for i in range(2, factor):
        if (factor % i) == 0:
            return False
    return True


print(sacar_factores(600851475143))