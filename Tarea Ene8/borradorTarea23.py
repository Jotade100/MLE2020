def leerArchivo(nombre):
    """Lectura de archivo:
    Lee un archivo y retorna su contenido separado por líneas en un arreglo
    y a su vez separado por palabras"""
    return [line.rstrip('\n').split() for line in open(nombre)]

triangulo = leerArchivo("triangle.txt")

cola = [(0, 0)]
comodin = [[0 for y in range(0, x + 1)] for x in range(0, len(triangulo))]
comodin[0][0] = int(triangulo[0][0])

while len(cola) != 0:
    actual = cola.pop(0)
    # print(actual)
    for w in range(actual[1], actual[1] + 2):
        # print(actual[0] + 1, ',', w, end='\t')
        if comodin[actual[0] + 1][w] < (int(comodin[actual[0]][actual[1]]) + int(triangulo[actual[0] + 1][w])):
                comodin[actual[0] + 1][w] = int(comodin[actual[0]][actual[1]]) + int(triangulo[actual[0] + 1][w])  
        if((actual[0] + 1) < (len(triangulo) - 1)):
            cola.append((actual[0] + 1, w))
    # print()

# print(leerArchivo("triangle.txt"))
print(max(comodin[len(triangulo) - 1]))