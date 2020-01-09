import math
# Ejemplo que no es cuadrado
# tuplas = [(3, 0), (2, 1), (2, 2), (3, 2)]
# Ejemplos que sí son cuadrados
# tuplas = [(-2, 9), (4, 6), (1, 0), (-5, 3)]
tuplas = [(0, 1), (3, 5), (7, 2), (4, -2)]

def distancia(w, z):
    """Calcular la distancia:
    Se determina la longitud del vector formado por dos puntos"""
    return math.sqrt(((w[0]-z[0])**2)+((w[1]-z[1])**2))

def addIfNotInList(lista, elemento):
    """Ingreso excluyente:
    Se añade el elemento únicamente si no se encuentra en la lista"""
    if elemento not in lista:
        lista.append(elemento)

# El método fue diseñado considerando que los vértices no son entregados de manera ordenada.

def determinarSiEsCuadrado(tuplas):
    """Determina si 4 vértices conforman un cuadrado:
    Calculando las distancias vectoriales entre distintas combinaciones de 
    vértices se determina si es cuadrado"""
    rectas = []
    for x in range(3):
        for y in range (x+1, 4):    
            addIfNotInList(rectas, distancia(tuplas[x], tuplas[y]))
    # Si sólo hay dos elementos (lado y diagonal) es un cuadrado
    if len(rectas) != 2:
        print("No es un cuadrado")
    else:
        print("Sí es un cuadrado")

determinarSiEsCuadrado(tuplas)

