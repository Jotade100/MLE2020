import numpy as np
import random as rnd


def derivada_teta_1(tetas, x, y, param):
    """Realiza la derivada de la función de costo
        para cualquier parámetro teta
    """
    return (((np.dot(tetas, x) - y) * x[param]).sum()) / (len(x))


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
tetas = [1.0, 1.0]
x, y = gen_data(50, 10, 25)
x = [[1 for i in range(len(x))], x]  # relleno la primera fila con 1 para el intercepto
# Uso numpy para realizar operaciones con matrices y que sea más rápida
#   la sumatoria de la función costo
tetas = np.array(tetas)
x = np.array(x, dtype=np.float64)
y = np.array(y)
print(x, y)
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
    derivadas = []
    for i in range(len(teta_gradiente)):
        derivadas.append(derivada_teta_1(teta_temporal, x, y, i))
        teta_gradiente[i] -= razon_de_aprendizaje * derivadas[i]
    if (abs(sum(derivadas) / len(derivadas)) < tolerancia) or (numero_de_iteraciones_maximo == 0):
        converger = False



print(teta_gradiente)