import time

num_conjuntos = 2
cache_size = 10
cache = [[0, 0]] * cache_size
idxo = [0] * num_conjuntos
total = 0
aciertos = 0
fallos = 0


def exp(n):
    global total, aciertos, fallos, idxo
    total += 1
    idxc = n % num_conjuntos
    p = int(cache_size / num_conjuntos)
    for i in range(idxc * p, idxc * p + p):
        if cache[i][0] == n:
            aciertos += 1
            return cache[i][0]
    
    fallos += 1
    res = 1
    for i in range(n):
        res *= n

    idx = (idxc * p) + idxo[idxc]
    cache[idx] = [n, res]

    if idxo[idxc] == p - 1:
        idxo[idxc] = 0
    else:
        idxo[idxc] += 1

    return res


if __name__ == '__main__':
    lista_n = [5000, 220, 457, 12, 10000, 323, 10000, 440, 323, 5000, 220, 440] * 5

    for num in lista_n:
        inicio = time.perf_counter()
        resultado = exp(num)
        fin = time.perf_counter()

        print(f"El resultado de ejecutar la exponencial de {num} es {fin - inicio} segundos")
    
    aciertos_porcentaje = (float(aciertos) / float(total)) * 100.0
    fallos_porcentaje = (float(fallos) / float(total)) * 100.0

    print(f"aciertos: {aciertos}")
    print(f"fallos: {fallos}")

    print(f"El porcentaje de aciertos es {aciertos_porcentaje}% y el porcentaje de fallos es {fallos_porcentaje}%")
