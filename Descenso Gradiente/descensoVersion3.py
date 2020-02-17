import numpy as np
import random as rnd


def derivada_teta_1(tetas, x, y):
    """Realiza la derivada de la función de costo
        para cualquier parámetro teta
    """
    return np.dot(x, np.dot(tetas, x) - y) / len(y)

def funcion_costo(tetas, x, y):
    """Realiza la función de costo
        para cualquier parámetro teta
    """
    return (np.sum(np.dot(tetas, x) - y) ** 2) / 2*  len(y)


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

def gen_data_funcion(n, m, b):
    """Sirve para generar datos a partir de una función.
        y = m * x + b
    """
    x = []
    y = []
    for i in range(0, n):
        x.append(i)
        y.append(i * m + b)
    return x, y

def imprimir_resultados(teta, x, y):
    """Sirve para imprimir la lista de tetas y el costo según
        estos usando como base la función de costo.
    """
    for i in range(len(teta)):
        print("\u03B8{sub} = {value}".format(sub = i + 1, value = teta[i]))
    print("El costo es: {}".format(funcion_costo(teta_gradiente, x, y)))


# Datos iniciales
tetas = [rnd.uniform(0, 1), rnd.uniform(0, 1)] # Genero números aleatorios para Teta
x, y = gen_data_funcion(15, 5, 5)
x = [[1 for i in range(len(x))], x]  # relleno la primera fila con 1 para el intercepto
# Uso numpy para realizar operaciones con matrices y que sea más rápida
# la sumatoria de la función costo
tetas = np.array(tetas, dtype='float64')
x = np.array(x, dtype=np.float64)
y = np.array(y)
# variables de flujo del gradiente
razon_de_aprendizaje = 0.001
teta_gradiente = tetas.copy()
converger = True
numero_de_iteraciones_maximo = 10000
tolerancia = 0.01


while (converger):
    # hacer derivada de funcion
    # moverse en el espacio
    numero_de_iteraciones_maximo -= 1
    teta_temporal = teta_gradiente.copy()
    derivadas = derivada_teta_1(teta_temporal, x, y)
    teta_gradiente -= razon_de_aprendizaje * derivadas
    if (np.linalg.norm(derivadas) < tolerancia) or (numero_de_iteraciones_maximo == 0):
        converger = False



imprimir_resultados(teta_gradiente, x, y)