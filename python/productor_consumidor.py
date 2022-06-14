import random
import concurrent.futures
import threading


SENTINEL = object()

def productor(pipeline):
    for _ in range(10):
        message = random.randint(1, 101)
        print(f"Productor tiene el mensaje: {message}")
        pipeline.set_message(message, "Productor")

    pipeline.set_message(SENTINEL, "Productor")


def consumidor(pipeline):
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumidor")
        if message is not SENTINEL:
            print(f"Consumidor guarda el mensaje {message}")

class Pipeline:
    def __init__(self):
        self.message = 0
        self.productor_lock = threading.Lock()
        self.consumidor_lock = threading.Lock()
        self.consumidor_lock.acquire()
    
    def get_message(self, name):
        print(f"{name} a punto de conseguir el candado de get")
        self.consumidor_lock.acquire()
        print(f"{name} consiguio el candado de get")
        message = self.message
        print(f"{name} a punto de liberar el candado de set")
        self.productor_lock.release()
        print(f"{name} libero el candado de set")

        return message

    def set_message(self, message, name):
        print(f"{name} a punto de conseguir el candado de set")
        self.productor_lock.acquire()
        print(f"{name} consigui el candado de set")
        self.message = message
        print(f"{name} a punto de liberar el candado de get")
        self.consumidor_lock.release()
        print(f"{name} libero el candado de get")  


if __name__ == "__main__":
    pipeline = Pipeline()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(productor, pipeline)
        executor.submit(consumidor, pipeline)