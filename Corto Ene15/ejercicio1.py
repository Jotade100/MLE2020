lista_de_numeros = []


def invertir(numero):
    resultado = 0
    i = 0
    while numero > 0:
        i += 1
        resto = numero % 10
        resultado += resto * 10**i
        numero = int(numero / 10)
        
        

def detectar_palindromo(numero):
    arreglo_numero = [int(digito) for digito in str(numero)]