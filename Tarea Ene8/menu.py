diccionarioOp = {
    'suma': (lambda x, y: x+y), 
    'resta': (lambda x, y: x-y), 
    'multiplicación': (lambda x, y: x*y)
    }

def generarMenu(dic):
    """Generar el menú automáticamente:
    Selecciona los elementos según su posición en el diccionario"""
    print("Seleccione una opción: ")
    # Se guarda en forma de lista los elementos del diccionario
    enumeracion = list(enumerate(dic))
    for x,y in enumeracion:
        print("\t {} ~ {}".format(x, y))
    seleccion = int(input("Introduzca una opción: "))
    if seleccion not in range(len(enumeracion)):
        print("Opción no válida")
    else: 
        resultado = dic.get(enumeracion[seleccion][1])
        print("Resultado: {}".format( resultado(int(input("Introduzca el primer operando: ")), int(input("Introduzca el segundo operando: ")))))

generarMenu(diccionarioOp)