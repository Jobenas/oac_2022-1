import time

def pot(x):
    val = 1

    for _ in range(x):
        val *= x

    return val


if __name__ == '__main__':
    nums = [x for x in range(30000, 30032)]
    # print(nums)
    resultados = []

    inicio = time.perf_counter()
    for num in nums:
        resultados.append(pot(num))
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
