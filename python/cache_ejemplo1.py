import time

cache = dict()
aciertos = 0
fallos = 0
total = 0

def factorial_cache(n):
    global aciertos, fallos, total
    total += 1
    if n in cache.keys():
        aciertos += 1
        return cache[n]
    
    fallos += 1

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
    print(f"El tiempo de ejecucion para la funcion sin cache en el rango de {inicio} - {fin - 1} es {fin_normal - inicio_normal} segundos")

    inicio_cache = time.perf_counter()
    for num in range(inicio, fin):
        res = factorial_cache(num)
    fin_cache = time.perf_counter()
    print(f"El tiempo de ejecucion para la funcion con cache en el rango de {inicio} - {fin - 1} es {fin_cache - inicio_cache} segundos")

    aciertos_porcentaje = (float(aciertos) / float(total)) * 100.0
    fallos_porcentaje = (float(fallos) / float(total)) * 100.0

    print(f"aciertos: {aciertos}")
    print(f"fallos: {fallos}")

    print(f"El porcentaje de aciertos es {aciertos_porcentaje}% y el porcentaje de fallos es {fallos_porcentaje}%")