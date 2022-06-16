import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def get_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: leyo {len(response.content)} bytes de {url}")


def get_all(sites):
    with multiprocessing.Pool(initializer=set_global_session, processes=multiprocessing.cpu_count()) as pool:
        pool.map(get_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    inicio = time.perf_counter()
    get_all(sites)
    fin = time.perf_counter()

    print(f"Descarga completa en {fin - inicio} segundos")
