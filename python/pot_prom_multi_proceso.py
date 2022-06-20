from concurrent.futures import process
import time
import multiprocessing as mp

def func(x):
    val = 1

    val = x * 2

    time.sleep(0.05)
    
    return val


if __name__ == '__main__':
    nums = [x for x in range(100, 200)]
    acc = 0
    p = mp.Pool(processes=mp.cpu_count())

    inicio = time.perf_counter()
    resultados = p.map(func, nums)
    p.close()
    p.join()
    for resultado in resultados:
        acc += resultado
    prom = acc / len(nums)
    fin = time.perf_counter()

    print(f"Resultado: {prom}. Tiempo total de ejecucion: {fin - inicio} segundos")