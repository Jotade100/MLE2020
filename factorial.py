import time as time

def factorial(n):
    for i in range(1, n):
        time.sleep(1)
        n *= i
    return n


def memoize(slow_function):
    cache = {}
    def funcion_con_cache(*x):
        llave = '-'.join([str(arg)] for arg in x)
        if llave not in cache:
            cache[llave] = slow_function(*x)
        return cache[llave]
    return funcion_con_cache
        
    

print(memoize(factorial)(4))

print(memoize(factorial)(2))

print(memoize(factorial)(4))