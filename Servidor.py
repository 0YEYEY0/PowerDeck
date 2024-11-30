import socket
import threading
import uuid

# Lista para manejar jugadores en espera
jugadores_espera = {}

# Bloqueo para manejo seguro de listas entre hilos
lock = threading.Lock()

# Configuracion del servidor
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Puerto de escucha


# Funcion que maneja cada conexion de cliente
def manejo_cliente(conn, addr):
    cliente_id = str(uuid.uuid4())
    print(f"Conectado por {addr} con ID {cliente_id}")

    jugadores_espera[cliente_id] = {
        'conn': conn,
        'addr': addr,
        'en_busqueda': False
    }

    try:
        while True:
            data = conn.recv(1024).decode()

            if data == 'buscar_partida':
                with lock:
                    jugadores_espera[cliente_id]['en_busqueda'] = True
                    print(f"Jugador {cliente_id} agregado a la busqueda. Total en espera: {len(jugadores_espera)}")
                conn.sendall(b'Buscando partida')

                # Intentar emparejar si hay suficientes jugadores
                emparejar_jugadores()

            elif data == 'cancelar_busqueda':
                with lock:
                    jugadores_espera.clear()  # Vaciar la lista de espera
                    print("Lista de espera vaciada por cancelacion.")
                conn.sendall(b'Busqueda cancelada')

            elif data == 'volver_a_buscar':
                with lock:
                    jugadores_espera[cliente_id]['en_busqueda'] = True
                    print(f"Jugador {cliente_id} ha vuelto a buscar partida.")
                conn.sendall(b'Buscando partida')

    except Exception as e:
        print(f"Error con {addr}: {e}")
    finally:
        with lock:
            if cliente_id in jugadores_espera:
                del jugadores_espera[cliente_id]
        print(f"Conexion cerrada con {addr}")
        conn.close()


# Funcion para emparejar jugadores
def emparejar_jugadores():
    with lock:
        jugadores_disponibles = [id for id, datos in jugadores_espera.items() if datos['en_busqueda']]
        if len(jugadores_disponibles) >= 2:
            jugador1 = jugadores_disponibles.pop(0)
            jugador2 = jugadores_disponibles.pop(0)

            # Enviar mensaje a los jugadores emparejados
            try:
                jugadores_espera[jugador1]['conn'].sendall(b'En partida')  # Cambiado
                jugadores_espera[jugador2]['conn'].sendall(b'En partida')  # Cambiado
                print(
                    f"Partida encontrada entre {jugadores_espera[jugador1]['addr']} y {jugadores_espera[jugador2]['addr']}")
            except Exception as e:
                print(f"Error al enviar datos a los jugadores: {e}")


# Inicializacion del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor corriendo en {HOST}:{PORT}")

try:
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=manejo_cliente, args=(conn, addr))
        thread.start()
except KeyboardInterrupt:
    print("Servidor detenido manualmente")
finally:
    server.close()

