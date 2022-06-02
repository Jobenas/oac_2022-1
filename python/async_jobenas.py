import time

inicios = dict()

resultados = []

def jobenas_sleep(idx: int, secs: int):
    if not idx in inicios.keys():
        inicios[idx] = time.perf_counter()
        return False
    
    if (time.perf_counter() - inicios[idx]) >= secs:
        return True
    else:
        return False


def cuenta(idx: int):
    if not idx in inicios.keys():
        print(f"[{idx}] Uno")
    
    res = jobenas_sleep(idx, 1)

    if res:
        print(f"[{idx}] Dos")
    
    return res


if __name__ == "__main__":
    resultados = [False, False, False]
    inicio = time.perf_counter()
    while not resultados[0] and not resultados[1] and not resultados[2]:
        if not resultados[0]:
            resultados[0] = cuenta(0)
        if not resultados[1]:
            resultados[1] = cuenta(1)
        if not resultados[2]:
            resultados[2] = cuenta(2)
    fin = time.perf_counter()

    print(f"El programa ejecuto en {fin - inicio} segundos")