def numero_par(numero):
    return 0 == numero % 2


def suma_fibonacci_pares_menores_cuatro_millones():
    resultado = 0
    x = 1
    y = 2
    while x < 4000000:
        if numero_par(x):
            resultado += x
        x, y = y, y + x
    return resultado

print(suma_fibonacci_pares_menores_cuatro_millones())