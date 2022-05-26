import socket
import time

SOCK_BUFFER = 1024

if __name__ == '__main__':
    data_a_enviar = input("Por favor tipee algo: ")

    inicio = time.perf_counter()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor en {server_address[0]}, en puerto {server_address[1]}")
    sock.connect(server_address)

    try:
        print("Enviando datos al servidor")
        # sock.sendall(b'Hola Mundo')
        sock.sendall(data_a_enviar.encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
    except Exception as e:
        print(f"Sucedio algo: {e}")
    finally:
        print("Cerrando conexion")
        sock.close()
    
    fin = time.perf_counter()

    print(f"Recibi: {data}, en {fin - inicio} segundos")
    print("Finalizando programa")