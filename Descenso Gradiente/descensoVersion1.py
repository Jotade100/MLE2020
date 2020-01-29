import numpy as np

def derivada_teta_1(tetas, x, y, param):
    return (((np.dot(tetas, x) - y) * x[param]).sum()) / (len(x))


# Datos iniciales
tetas = [2.0, 1.0]
x = [[1.0, 1.0], [4.0, 1.0]] # relleno la primera fila con 1 para el intercepto
y = [9, 10]
# Uso numpy para realizar operaciones con matrices y que sea más rápida
#   la sumatoria de la función costo
tetas = np.array(tetas)
x = np.array(x)
y = np.array(y)
# variables de flujo del gradiente
razon_de_aprendizaje = 1
teta_gradiente = tetas.copy()
converger = True



while (converger):
    # hacer derivada de funcion
    # moverse en el espacio
    teta_temporal = teta_gradiente.copy()
    derivadas = []
    for i in range(len(teta_gradiente)):
        derivadas.append(derivada_teta_1(teta_temporal, x, y, i))
        teta_gradiente[i] -= razon_de_aprendizaje * derivadas[i]




print(teta_gradiente)