def numero_mas_pequeño_divisible_por(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = minimo_comun_multiplo(resultado, i)
    return resultado
        

def maximo_comun_divisor(numero1, numero2):
    while numero2:
        mcd = numero2
        numero2 = numero1 % numero2
        numero1 = mcd
    return mcd

def minimo_comun_multiplo(numero1, numero2):
    return numero1 * numero2 / maximo_comun_divisor(numero1, numero2)

print(numero_mas_pequeño_divisible_por(10))