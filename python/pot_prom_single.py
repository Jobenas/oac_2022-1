import time

def func(x):
    val = 1

    val = x * 2

    time.sleep(0.05)
    
    return val


if __name__ == '__main__':
    nums = [x for x in range(100, 200)]
    acc = 0

    inicio = time.perf_counter()
    for num in nums:
        acc += func(num)
    prom = acc / float(len(nums))
    fin = time.perf_counter()

    print(f"Resultado: {prom}. Tiempo total de ejecucion: {fin - inicio} segundos")