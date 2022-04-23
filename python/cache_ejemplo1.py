import time

cache = dict()

def factorial_cache(n):
    if n in cache.keys():
        return cache[n]
    
    fact = None
    if n== 1:
        fact = 1
    else:
        fact = n * factorial_cache(n - 1)

    cache[n] = fact
    return fact

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    inicio = 500
    fin = 901
    inicio_normal = time.perf_counter()
    for num in range(inicio, fin):
        res = factorial(num)
    fin_normal = time.perf_counter()
    print(f"El tiempo de ejecucion para la funcion sin cache en el rango de {inicio} - {fin} es {fin_normal - inicio_normal} segundos")

    inicio_cache = time.perf_counter()
    for num in range(inicio, fin):
        res = factorial_cache(num)
    fin_cache = time.perf_counter()
    print(f"El tiempo de ejecucion para la funcion con cache en el rango de {inicio} - {fin} es {fin_cache - inicio_cache} segundos")
