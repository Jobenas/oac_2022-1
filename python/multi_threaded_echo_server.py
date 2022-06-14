import socket
from threading import Thread

SOCK_BUFFER = 1024

num_hilos = 0

def client_handler(conn, client_address):
    global num_hilos

    num_hilos += 1
    print(f"El numero de hilos en ejecucion en este momento es {num_hilos}")
    
    try:
        print(f"Conexion de {client_address}")

        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data} de {client_address}")
                conn.sendall(data)
            else:
                break
    except Exception as e:
        print(f"Excepcion {e}")
    finally:
        print("Cliente cerro la conexion")
        conn.close()

    num_hilos -= 1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('0.0.0.0', 5000)
    print(f"Iniciandop servidor en {server_address[0]}, en el puerto {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("esperando conexiones")
        
        conn, client_address = sock.accept()

        t = Thread(target=client_handler, args=(conn, client_address))
        t.start()