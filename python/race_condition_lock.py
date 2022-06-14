import time
import concurrent.futures
import threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    
    def update(self, name):
        print(f"Thread {name} iniciando actualizacion")
        print(f"Thread {name} esta a punto de generar un candado")
        # with self._lock:
        self._lock.acquire()
        print(f"Thread {name} tiene el candado")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        print(f"Thread {name} a punto de liberar el candado")
        self._lock.release()
        print(f"Thread {name} libero el candado")
        print(f"Thread {name} ha terminado la actualizacion")


if __name__ == "__main__":
    workers = 2
    db = FakeDatabase()
    print(f"Valor inicial de la base de datos: {db.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    
    print(f"Valor final de la base de datos: {db.value}")