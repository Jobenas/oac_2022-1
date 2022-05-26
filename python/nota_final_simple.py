import time

labs = []
e1 = 0
e2 = 0
nl = 0

if __name__ == '__main__':
    inicio = time.perf_counter()

    inicio_es = time.perf_counter()
    for i in range(10):
        nota = input(f"Ingrese la nota del laboratorio {i + 1}: ")
        labs.append(int(nota))
    
    e1 = int(input("Por favor ingrese la nota del examen 1: "))
    e2 = int(input("Por favor ingrese la nota del examen 2: "))
    fin_es = time.perf_counter()

    inicio_cpu = time.perf_counter()
    for lab in labs:
        nl += lab
    
    nl /= 10

    nota_final = ((3 * nl) + (3 * e1) + (3 * e2)) / 9
    fin_cpu = time.perf_counter()
    fin = time.perf_counter()

    print(f"La nota final del curso es {nota_final}")
    print(f"El tiempo total de ejecucion del programa es: {fin - inicio} segundos")
    print(f"Tiempo total de operaciones de E/S: {fin_es - inicio_es} segundos")
    print(f"Tiempo total de CPU: {fin_cpu - inicio_cpu} segundos")