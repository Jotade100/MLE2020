def multiplo_tres(numero):
    return (0 == numero % 3)

def multiplo_cinco(numero):
    return (0 == numero % 5)

def suma_multiplos_tres_cinco(numero):
    resultado = 0
    for i in range(1, numero + 1):
        if multiplo_cinco(i) or multiplo_tres(i):
            resultado += i
    return resultado

