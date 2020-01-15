nombres = {
    'millares': ["", "un mil"],
    'centenas': ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"],
    'decenas': ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"],
    'unidades': ["" ,"uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"],
}

def numero_a_letras(numero):
    """ Función que convierte el número indicado
    a su forma en letras. Ejemplo:
    Para el número 528: Quinientos veinte y ocho"""
    arreglo_numero = [int(digito) for digito in str(numero)]
    unidades, decenas, centenas, millares = "", "", "", ""
    if len(arreglo_numero) == 4:
        millares = nombres['millares'][arreglo_numero[0]]
        arreglo_numero.pop(0)
    if len(arreglo_numero) == 3:
        centenas = nombres['centenas'][arreglo_numero[0]]
        arreglo_numero.pop(0)
    if len(arreglo_numero) == 2:
        if arreglo_numero[0] > 1:
            decenas = nombres['decenas'][arreglo_numero[0]]
            arreglo_numero.pop(0)
            if arreglo_numero[0] != 0:
                decenas += " y"
        else:
            arreglo_numero[0] = arreglo_numero[0] * 10  + arreglo_numero.pop(1)
    if numero > 0:
        unidades = nombres['unidades'][arreglo_numero[0]]
    else:
        unidades = "cero"
    print("El número es {m} {c} {d} {u}".format(m = millares,
                                                c = centenas,
                                                d = decenas,
                                                u = unidades))
    

print(numero_a_letras(120))
    


