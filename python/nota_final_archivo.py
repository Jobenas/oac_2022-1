import time

nombre_archivo = "notas.csv"

e1 = 0
e2 = 0
nl = 0

promedios = []
tiempos_es = []
tiempos_cpu = []

codigos = ["20220001", "20220002", "20220003", "20220004", "20220005", "20220006"]

contenido = None

def get_data(codigo: str) -> list[str]:
    global contenido

    if contenido is None:
        f = open(nombre_archivo, 'r')
        contenido = f.read()
        f.close()

    data = contenido.split("\n")
    
    for line in data:
        code = line.split(",")
        if code[0] == codigo:
            return code
    
    return []


if __name__ == "__main__":
    inicio = time.perf_counter()

    for codigo in codigos:
        inicio_es = time.perf_counter()
        notas = get_data(codigo)
        fin_es = time.perf_counter()
        tiempos_es.append(fin_es - inicio_es)

        inicio_cpu = time.perf_counter()
        for i in range(1, len(notas) - 2):
            nl += int(notas[i])
        nl /= 10

        e1 = int(notas[-2])
        e2 = int(notas[-1])

        nota_final = ((3 * nl) + (3 * e1) + (3 * e2)) / 9
        fin_cpu = time.perf_counter()
        tiempos_cpu.append(fin_cpu - inicio_cpu)
        promedios.append(nota_final)

    fin = time.perf_counter()

    print(f"Las nota finales del curso son {promedios}")
    print(f"El tiempo total de ejecucion del programa es: {fin - inicio} segundos")
    print(f"Los tiempos de operaciones de E/S: {tiempos_es}")
    print(f"Los tiempos de CPU: {tiempos_cpu}")