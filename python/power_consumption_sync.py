from itertools import accumulate
import time
from datetime import datetime, timedelta


def leer_archivo(archivo: str = "household_power_consumption.csv") -> str:
    f = open(archivo, "r")
    contenido = f.read()
    f.close()

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
            print(f"Calculando dia: {ts.date()}")
        if indice != -1:
            convertido, indice = encuentra_data(data, ts, ts + timedelta(minutes=15), indice)
        else:
            convertido, indice = encuentra_data(data, ts, ts + timedelta(minutes=15))
        energia_activa = acumula_valores(convertido, 1)
        energia_reactiva = acumula_valores(convertido, 2)
        datos.append([ts, energia_activa, energia_reactiva])
        ts += timedelta(minutes=15)

    return datos

if __name__ == "__main__":
    data = leer_archivo()
    headers, data = separa_filas(data)
    ts_inicio = datetime(year=2006, month=12, day=16, hour=17, minute=15, second=0)
    ts_fin = datetime(year=2010, month=11, day=26, hour=21, minute=15, second=0)

    # ts_inicio = datetime(year=2006, month=12, day=17, hour=0, minute=0, second=0)
    # ts_fin = datetime(year=2006, month=12, day=17, hour=0, minute=15, second=0)

    inicio = time.perf_counter()
    datos = convierte_15_minutos(data, ts_inicio, ts_fin)
    fin = time.perf_counter()

    print(len(datos))
    print(datos[0])
    print(datos[-1])
    print(f"Tiempo de ejecución: {fin - inicio} segundos")
