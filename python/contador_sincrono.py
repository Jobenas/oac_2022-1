import time
import random

def cuenta(idx: int):
    print(f"[{idx}] Uno")
    time.sleep(random.randint(1, 5))
    # time.sleep(1)
    print(f"[{idx}] Dos")

def main():
    for i in range(10):
        cuenta(i)

if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"El programa ejecuto en {fin - inicio} segundos")