import asyncio
import time
import random


async def cuenta(idx: int):
    print(f"[{idx}] Uno")
    # await asyncio.sleep(1)
    await asyncio.sleep(random.randint(1, 5))
    print(f"[{idx}] Dos")


async def main():
    await asyncio.gather(*(cuenta(i) for i in range(10)))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"El programa ejecuto en {fin - inicio} segundos")
