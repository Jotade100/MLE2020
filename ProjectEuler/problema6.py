def cuadrado_de_la_suma_de_los_numeros(numero):
    return ((numero * (numero + 1)) / 2)**2

def suma_de_cuadrados(numero):
    return ((numero * (numero + 1) * ((2 * numero) + 1)) / 6)

print(cuadrado_de_la_suma_de_los_numeros(100) - suma_de_cuadrados(100))