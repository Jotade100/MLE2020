def es_palindromo(numero):
    return numero == revertir(numero)


def revertir(numero):
    revertido = 0
    while(numero > 0):
        restante = numero % 10
        revertido = (revertido * 10) + restante
        numero = numero //10
    return revertido


def palindromo_mas_grande_producto_tres_digitos():
    for x in range(999, 500, -1):
        for y in range(99, 0, -1):
            if es_palindromo(x * y):
                return x * y

print(palindromo_mas_grande_producto_tres_digitos())