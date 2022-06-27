import time
from datetime import datetime, timedelta
import multiprocessing as mp


def leer_archivo(archivo: str = "household_power_consumption.csv") -> str:
    with open(archivo, "r") as f:
        contenido = f.read()
    
    return contenido


def separa_filas(contenido: str) -> list:
    filas = contenido.split("\n")
    cabecera = filas[0]
    filas = filas[1:]
    return cabecera, filas


def separa_columnas(fila: str) -> list:
    columnas = fila.split(",")
    for idx in range(len(columnas)):
        if idx == 0:
            columnas[idx] = datetime.strptime(columnas[idx], "%Y-%m-%d %H:%M:%S")
        else:
            columnas[idx] = float(columnas[idx])
    return columnas


def encuentra_data(data: list[str], timestamp_inicio: datetime, timestamp_fin: datetime, init_idx: int = 0) -> list:
    valores = []
    final_idx = -1
    for idx in range(init_idx, len(data)):
        fila = data[idx]
        fila = separa_columnas(fila)
        if timestamp_inicio <= fila[0] <= timestamp_fin:
            valores.append(fila)
        if timestamp_fin < fila[0]:
            final_idx = idx
            break
    return valores, final_idx


def acumula_valores(data: list, columna: int) -> float:
    return sum(fila[columna] for fila in data)


def convierte_15_minutos(data: list[str], ts_start: datetime, ts_end: datetime) -> list:
    datos = []
    ts = ts_start
    indice = 0
    while ts < ts_end:
        if ts.hour == 0 and ts.minute == 0 and ts.second == 0:
            # print(f"Calculando dia: {ts.date()}")
            pass
        if indice != -1:
            convertido, indice = encuentra_data(data, ts, ts + timedelta(minutes=15), indice)
        else:
            convertido, indice = encuentra_data(data, ts, ts + timedelta(minutes=15))
        energia_activa = acumula_valores(convertido, 1)
        energia_reactiva = acumula_valores(convertido, 2)
        datos.append([ts, energia_activa, energia_reactiva])
        ts += timedelta(minutes=15)

    return datos

def busca_inicio_anho(data: list[str], anho: int):
    for idx in range(len(data)):
        fila = data[idx]
        fila = separa_columnas(fila)
        if fila[0].year == anho:
            return idx
    return -1

if __name__ == "__main__":
    data = leer_archivo()
    headers, data = separa_filas(data)
    idxs = [0, 21996, 547596, 1074636, 1600236]
    num_bloque = 8
    
    sub_data = []
    for i in range(len(idxs)):
        if i < len(idxs) - 1:
            sub_data.append(data[idxs[i]:idxs[i+1]])
        else:
            sub_data.append(data[idxs[i]:])

    fechas_inicio = [datetime.strptime(b[0].split(",")[0], "%Y-%m-%d %H:%M:%S") for b in sub_data]
    fechas_fin = [datetime.strptime(b[-1].split(",")[0], "%Y-%m-%d %H:%M:%S") for b in sub_data]

    args = zip(sub_data, fechas_inicio, fechas_fin)
    p = mp.Pool(processes=mp.cpu_count())

    inicio = time.perf_counter()
    resultados = p.starmap(convierte_15_minutos, args)
    fin = time.perf_counter()
    print(resultados[0][0])
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
