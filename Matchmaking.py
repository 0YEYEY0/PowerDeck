import tkinter as tk
import socket
import threading
import time

# Variables globales
buscando = False
conexion = None  # Manejar conexión activa con el servidor

def buscar_partida():
    global buscando
    if buscando:  # Evitar múltiples búsquedas simultáneas
        return

    buscando = True
    estado_var.set("Buscando partida...")
    thread = threading.Thread(target=conectar_al_servidor, daemon=True)
    thread.start()

def conectar_al_servidor():
    global buscando, conexion
    start_time = time.time()

    try:
        conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexion.connect(('127.0.0.1', 12345))  # Conectar al servidor
        conexion.sendall(b'buscar_partida')

        while buscando:
            # Verificar si ha pasado el tiempo límite de 60 segundos
            if time.time() - start_time > 60:
                estado_var.set("Tiempo excedido")
                buscando = False
                return

            conexion.settimeout(1)  # Timeout corto para no bloquear indefinidamente
            try:
                data = conexion.recv(1024).decode()
                if data == 'En partida':
                    estado_var.set("¡Partida encontrada!")
                    buscando = False
                    break
                elif data == 'Búsqueda cancelada':
                    estado_var.set("Búsqueda cancelada")
                    buscando = False
                    break
            except socket.timeout:
                continue

    except Exception as e:
        if buscando:
            estado_var.set("Error de conexión")
            print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
            conexion = None
        buscando = False

def cancelar_busqueda():
    global buscando, conexion
    if not buscando:
        return

    buscando = False
    estado_var.set("Cancelando búsqueda...")

    try:
        if conexion:
            conexion.sendall(b'cancelar_busqueda')  # Informar al servidor
    except Exception as e:
        print(f"Error al cancelar: {e}")
    finally:
        if conexion:
            conexion.close()
            conexion = None
        estado_var.set("Búsqueda cancelada")

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Matchmaking")
root.geometry("400x300")

estado_var = tk.StringVar()
estado_var.set("Desconectado")

# Botón de buscar partida
boton_buscar = tk.Button(root, text="Buscar Partida", command=buscar_partida)
boton_buscar.pack(pady=10)

# Botón para cancelar la búsqueda
boton_cancelar = tk.Button(root, text="Cancelar Búsqueda", command=cancelar_busqueda)
boton_cancelar.pack(pady=10)

# Etiqueta de estado
estado_label = tk.Label(root, textvariable=estado_var)
estado_label.pack(pady=5)

root.mainloop()
