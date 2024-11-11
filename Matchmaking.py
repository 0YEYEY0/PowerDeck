import tkinter as tk
import socket
import threading
import time

# Variable para controlar la búsqueda
buscando = False


def buscar_partida():
    global buscando
    buscando = True
    estado_var.set("Buscando partida")
    thread = threading.Thread(target=conectar_al_servidor)
    thread.start()


def conectar_al_servidor():
    start_time = time.time()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', 12345))  # Conectar al servidor
            s.sendall(b'buscar_partida')

            while buscando:
                # Verificar si ha pasado el tiempo límite de 60 segundos
                if time.time() - start_time > 5:
                    estado_var.set("Tiempo excedido")
                    buscando = False
                    return

                data = s.recv(1024).decode()
                if data:
                    estado_var.set(data)
                    if data == 'En partida':
                        break
    except Exception as e:
        estado_var.set("Error de conexión")
        print(f"Error: {e}")


def cancelar_busqueda():
    global buscando
    buscando = False
    estado_var.set("Búsqueda cancelada")


# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Matchmaking")
root.geometry("400x300")  # Aumentar el tamaño de la ventana

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
