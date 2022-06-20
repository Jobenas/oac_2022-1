import time
import multiprocessing as mp

def pot(x):
    val = 1

    for _ in range(x):
        val *= x

    return val

if __name__ == '__main__':
    nums = [x for x in range(30000, 30032)]
    resultados = []
    procesos = []

    inicio = time.perf_counter()
    for num in nums:
        p = mp.Process(target=pot, args=(num, ))
        p.start()
        procesos.append(p)
    
    for p in procesos:
        p.join()

    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")

