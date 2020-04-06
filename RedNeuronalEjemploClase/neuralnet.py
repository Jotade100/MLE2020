# Importación de librerías
import numpy as np
import random as rnd

# Funciones importantes (Obtenidas del laboratorio de sigmoide)
def derivada_teta(tetas, x, y):
    """Realiza la derivada de la función de costo
        para cualquier parámetro teta
    """
    return np.dot(x, funcion_h(tetas, x) - y) / len(y)

def funcion_h(tetas, x):
    """Realiza la función sigmoide
        para cualquier parámetro teta
    """
    return np.power((1 + np.exp(-1 * np.dot(tetas.T, x)) ), -1) 

def funcion_g(tetas, a): # Propia de clase con Samuel Chávez 
    """Realiza la función sigmoide
        para cualquier parámetro teta y su capa a
    """
    return np.power((1 + np.exp(-1 * np.dot(tetas.T, a)) ), -1) 

def funcion_costo(tetas, x, y):
    """Realiza la función de costo
        para cualquier parámetro teta
    """
    return (np.dot(y, np.log(funcion_h(tetas, x))) + np.dot((1-y), np.log(1 - funcion_h(tetas, x)))  ) / -len(y)




### Variables de inicio
n = [] # número de neuronas de cada capa, 
# para n[0] sería el número de atributos y para n[última] sería la cantidad de variables a predecir
a = [] # activaciones
# a[0] corresponde a x 
# a[última] corresponde a nuestra predicción
thetas = [] #tetas de las distintas capas
datos = 1000

Deltas = [] # su forma es del mismo tamaño que Thetas
deltas = [] # corresponde al delta minúscula
Des = [] # corresponde a D


# haciendo el ciclo de forward

def feed_forward(tetas, x):
    """Va de capa en capa llenando las activaciones y llenando a
    """
    global a
    a[0] = x
    for i in range(len(tetas)):
        a.append(
            funcion_g(
                tetas[i],
                np.c_[np.ones(len(a[i])), a[i]]
            )
        )

def pasosRedNeural(x, y):
    global Deltas, deltas, a, thetas, Des
    deltas[len(n) - 1] = a[len(n) - 1] - y
    for l in reversed(range(1, len(n))):
        Deltas[l] = 0
        deltas[l] = np.dot(thetas[l][1:], deltas[l + 1]) * (np.dot(a[l], 1 -a[l]))
        Deltas[l] = Deltas[l] + np.dot(deltas[l + 1], a[l].T)
        Des[l] = (1/datos) * Deltas[l]






