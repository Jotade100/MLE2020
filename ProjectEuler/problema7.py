def criba_eratostenes(n):
    multiplos = set()
    primo = 0
    i = 2
    total = n**2
    while n > 0:
        if i not in multiplos:
            primo = i
            n -= 1
            multiplos.update(range(i*i, total, i))
        i += 1
    return primo
        


print(criba_eratostenes(6))