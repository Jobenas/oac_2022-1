import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def get_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Lei {len(response.content)} bytes de {url}")


def get_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(get_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 80

    inicio = time.perf_counter()
    get_all(sites)
    fin = time.perf_counter()

    print(f"Descarga completa en {fin - inicio} segundos")