from random import randint
import time

limite = 500

rand_min = 10
rand_max = 50

if __name__ == '__main__':
    inicio = time.perf_counter()
    valor = 0
    for i in range(limite):
        valor += (i + 1) * randint(rand_min, rand_max)
    
    valor = valor / limite

    fin = time.perf_counter()

    print(f"El valor del promedio ponderado es: {valor} y el tiempo de ejecucion es {fin - inicio} segundos")
