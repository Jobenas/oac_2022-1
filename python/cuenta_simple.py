import time
import random

CUENTA = 100000000

valor_inicio = random.randint(1, 20)

def imprime_inicio():
    global valor_inicio

    print(f"El valor inicial de la variable es {valor_inicio}")

def cuenta(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    # imprime_inicio()
    inicio = time.perf_counter()
    cuenta(CUENTA)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")