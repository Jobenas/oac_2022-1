import time
import numpy as np
import random
from itertools import repeat
from multiprocessing import Pool, cpu_count

M = 5000
N = 5000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(y)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == '__main__':
    resultado_serial = []

    mat_M = np.random.randint(100, size=(M,N))
    vector_A = np.random.randint(100, size=(N))

    # operacion serial
    inicio = time.perf_counter()
    for vector in mat_M:
        res_parcial = mult_vector_vector(vector, vector_A)
        resultado_serial.append(res_parcial)
    fin = time.perf_counter()
    print(f"Tiempo total de ejecucion en operacion serial: {fin - inicio} segundos")

    # operacion paralela
    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count())
    resultado_paralelo = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion en operacion paralela: {fin - inicio} segundos")

    print(f"Evaluacion de resultados es {resultado_serial == resultado_paralelo}")
