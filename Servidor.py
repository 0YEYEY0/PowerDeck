import socket
import threading
import time

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
    tiempo_inicio = time.time()  # Registrar el tiempo de inicio de la conexión

    try:
        conn.sendall(b'Desconectado')  # Estado inicial
        data = conn.recv(1024).decode()

        if data == 'buscar_partida':
            conn.sendall(b'Buscando partida')
            with lock:
                waiting_players.append((conn, addr))
                print(f"Jugador agregado. Total en espera: {len(waiting_players)}")

            # Esperar a que haya otro jugador o que se agote el tiempo de espera
            while True:
                with lock:
                    if len(waiting_players) >= 2:
                        # Emparejar los dos primeros jugadores de la lista
                        player1, addr1 = waiting_players.pop(0)
                        player2, addr2 = waiting_players.pop(0)

                        # Notificar a ambos jugadores que han encontrado partida
                        try:
                            player1.sendall(b'En partida')
                            player2.sendall(b'En partida')
                            print(f"Partida encontrada entre {addr1} y {addr2}")
                        except Exception as e:
                            print(f"Error al enviar datos a los jugadores: {e}")
                            player1.close()
                            player2.close()
                        return

                # Verificar si se ha excedido el tiempo de espera de 60 segundos
                if time.time() - tiempo_inicio > 60:
                    with lock:
                        if (conn, addr) in waiting_players:
                            waiting_players.remove((conn, addr))
                    conn.sendall(b'Tiempo excedido. No se encontro partida.')
                    conn.close()
                    print(f"Tiempo de espera agotado para la conexión con {addr}")
                    return

                time.sleep(1)  # Evitar un bucle muy intensivo

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

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