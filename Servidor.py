import socket
import threading

# Lista para manejar jugadores en espera
waiting_players = []

# Bloqueo para manejo seguro de listas entre hilos
lock = threading.Lock()

# Configuración del servidor
HOST = '127.0.0.1'  # Localhost
PORT = 12345  # Puerto de escucha


# Función que maneja cada conexión de cliente
def manejo_cliente(conn, addr):
    print(f"Conectado por {addr}")
    try:
        conn.sendall(b'Desconectado')  # Estado inicial
        data = conn.recv(1024).decode()

        if data == 'buscar_partida':
            conn.sendall(b'Buscando partida')
            with lock:
                waiting_players.append(conn)
                print(f"Jugador agregado. Total en espera: {len(waiting_players)}")

                if len(waiting_players) >= 2:
                    player1 = waiting_players.pop(0)
                    player2 = waiting_players.pop(0)

                    # Notificar a ambos jugadores que han encontrado partida
                    try:
                        player1.sendall(b'En partida')
                        player2.sendall(b'En partida')
                        print("Partida encontrada entre dos jugadores")
                    except Exception as e:
                        print(f"Error al enviar datos a los jugadores: {e}")
                        player1.close()
                        player2.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # No cierres `conn` aquí porque aún lo necesitas para la partida
        pass


# Inicialización del servidor
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
