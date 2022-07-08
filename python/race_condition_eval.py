import time
import concurrent.futures
from threading import Lock

class FakeDatabaseAtomic:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        print(f"Thread {name} iniciando actualizacion")
        local_copy = self.value
        local_copy += 1
        self.value = local_copy
        time.sleep(0.1)
        print(f"Thread {name} ha terminado la actualizacion")


class FakeDatabaseLock:
    def __init__(self):
        self.value = 0
        self._lock = Lock()
    
    def update(self, name):
        print(f"Thread {name} iniciando actualizacion")
        # print(f"Thread {name} esta a punto de generar un candado")
        with self._lock:
            # print(f"Thread {name} tiene el candado")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            # print(f"Thread {name} a punto de liberar el candado")
        # print(f"Thread {name} libero el candado")
        print(f"Thread {name} ha terminado la actualizacion")


if __name__ == "__main__":
    workers = 8
    iteraciones = 10
    tiempos_atomic = []
    tiempos_lock = []

    for i in range(iteraciones):
        db_atomic = FakeDatabaseAtomic()
        db_lock = FakeDatabaseLock()

        inicio_atomic = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for index in range(workers):
                executor.submit(db_atomic.update, index)
        fin_atomic = time.perf_counter()

        inicio_lock = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for index in range(workers):
                executor.submit(db_lock.update, index)
        fin_lock = time.perf_counter()

        tiempos_atomic.append(fin_atomic - inicio_atomic)
        tiempos_lock.append(fin_lock - inicio_lock)
    
    tiempo_atomic = sum(tiempos_atomic) / 10.0
    tiempo_lock = sum(tiempos_lock) / 10.0

    print(f"Tiempo atomic: {tiempo_atomic} segundos")
    print(f"Tiempo lock: {tiempo_lock} segundos")