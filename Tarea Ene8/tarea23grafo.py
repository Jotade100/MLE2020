def leerArchivo(nombre):
    """Lectura de archivo:
    Lee un archivo y retorna su contenido separado por líneas en un arreglo
    y a su vez separado por palabras"""
    return [line.rstrip('\n').split() for line in open(nombre)]


def calcularCaminoAdyLargo(triangulo):
    """Cálculo de camino de adyacentes:
    Tras recorrer un triángulo rectángulo de datos retorna el camino de
    adyacentes que suma más. [Algoritmo propuesto por Ing. Samuel Chávez]
    Su complejidad es de O(aristas + vertices) para el procesamiento.
    Su complejidad de almacenaje es el área del triángulo"""
    comodin = 0
    cola = [(0, 0, int(triangulo[0][0]))]
    while len(cola) != 0:
        actual = cola.pop()
        for w in range(actual[1], actual[1] + 2):
            if ((actual[0]) == (len(triangulo) - 1)):
                if comodin < actual[2]:
                    comodin = actual[2]
            if ((actual[0]) < (len(triangulo)-1)):
                cola.append((actual[0] + 1, w,
                            (actual[2] + int(triangulo[actual[0] + 1][w]))))
    return comodin

caminoMasLargo = calcularCaminoAdyLargo(leerArchivo("triangle.txt"))

print(
    "La suma más larga entre todos los caminos de "
    "adyacentes es {resultado}".format(resultado=caminoMasLargo)
)
