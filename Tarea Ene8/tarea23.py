def leerArchivo(nombre):
    """Lectura de archivo:
    Lee un archivo y retorna su contenido separado por líneas en un arreglo
    y a su vez separado por palabras"""
    return [list(map(int, line.split())) for line in open(nombre)]


def calcularCaminoAdyLargo(triangulo):
    """Cálculo de camino de adyacentes:
    Tras recorrer un triángulo rectángulo de datos retorna el camino de
    adyacentes que suma más. [Algoritmo propuesto por Ing. Samuel Chávez]
    Su complejidad es de O(lado^2).
    Su complejidad de almacenaje es el área del triángulo"""
    for y in range(len(triangulo) - 2, -1, -1):
        for x in range(0, y + 1):
            triangulo[y][x] += max(triangulo[y + 1][x: x + 2])
    return triangulo[0][0]


caminoMasLargo = calcularCaminoAdyLargo(leerArchivo("triangle.txt"))

print(
    "La suma más larga entre todos los caminos de "
    "adyacentes es {resultado}".format(resultado=caminoMasLargo)
)
