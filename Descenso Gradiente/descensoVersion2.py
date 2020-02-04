import numpy as np
import random as rnd


def derivada_teta_1(tetas, x, y):
    """Realiza la derivada de la función de costo
        para cualquier parámetro teta
    """
    return np.dot(x, np.dot(tetas, x) - y) / 2*len(y)


def gen_data(n, bias, varianza):
    """Sirve para generar datos de manera aleatoria.
        Idea tomada de Internet.
    """
    x = []
    y = []
    for i in range(0, n):
        x.append(i)
        y.append((i + bias) + rnd.uniform(0, 1) * varianza)
    return x, y


# Datos iniciales
tetas = [rnd.uniform(0, 1), rnd.uniform(0, 1)] # Genero números aleatorios para Teta
x, y = gen_data(10, 5, 5)
x = [[1 for i in range(len(x))], x]  # relleno la primera fila con 1 para el intercepto
# Uso numpy para realizar operaciones con matrices y que sea más rápida
#   la sumatoria de la función costo
tetas = np.array(tetas, dtype='float64')
x = np.array(x, dtype=np.float64)
y = np.array(y)
# variables de flujo del gradiente
razon_de_aprendizaje = 0.001
teta_gradiente = tetas.copy()
converger = True
numero_de_iteraciones_maximo = 1000
tolerancia = 1.5


while (converger):
    # hacer derivada de funcion
    # moverse en el espacio
    numero_de_iteraciones_maximo -= 1
    teta_temporal = teta_gradiente.copy()
    derivadas = derivada_teta_1(teta_temporal, x, y)
    teta_gradiente -= razon_de_aprendizaje * derivadas
    if (np.linalg.norm(derivadas) < tolerancia) or (numero_de_iteraciones_maximo == 0):
        converger = False


print(teta_gradiente)