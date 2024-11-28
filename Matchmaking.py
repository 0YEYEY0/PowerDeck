import tkinter as tk
import socket
import threading
import time
import json
import pygame
import os

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
                    return

                data = s.recv(1024).decode()
                if data:
                    estado_var.set(data)
                    if data == 'En partida':
                        iniciar_partida()
                        break
    except Exception as e:
        estado_var.set("Error de conexión")
        print(f"Error: {e}")

def iniciar_partida():
    pygame.init()
    # Definir dimensiones de la ventana
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Partida")

    # Leer el archivo del jugador
    try:
        with open('Jugadores/123_cuenta.json', 'r') as file:
            datos = json.load(file)
            mazo = datos.get('mazos', [])[0].get('cartas', [])  # Obtener cartas del primer mazo
            mano = mazo[:5]  # Tomar las primeras 5 cartas
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        mazo = []
        mano = []

    # Variables para almacenar las imágenes y las áreas de los botones
    cartas_imagenes = []
    botones_cartas = []

    # Cargar las imágenes de las cartas
    for carta in mano:
        try:
            # Obtener la ruta de la imagen desde el JSON
            ruta_imagen = carta.get('imagen', '')
            if not ruta_imagen:
                raise ValueError(f"No se encontró la imagen para la carta: {carta.get('nombre', 'Desconocida')}")

            # Verificar si el archivo existe
            if not os.path.exists(ruta_imagen):
                print(f"Imagen no encontrada en la ruta: {ruta_imagen}")
                continue

            # Cargar la imagen utilizando pygame
            imagen = pygame.image.load(ruta_imagen)

            # Redimensionar la imagen si es necesario (por ejemplo, 100x150 píxeles)
            imagen = pygame.transform.scale(imagen, (100, 150))

            # Añadir la imagen cargada a la lista
            cartas_imagenes.append(imagen)

            # Guardar el rectángulo donde se dibuja la carta para detectar clics
            botones_cartas.append(imagen.get_rect())

        except Exception as e:
            print(f"Error al cargar la imagen para {carta.get('nombre', 'Desconocida')}: {e}")

    # Coordenadas para mostrar las imágenes de las cartas
    x_offset = 50
    y_offset = 200

    # Ciclo principal de la ventana para mostrar las cartas
    running = True
    while running:
        # Gestionar eventos (como cerrar la ventana o hacer clic en las cartas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Detectar si el ratón hace clic en alguna carta
                mouse_x, mouse_y = event.pos
                for i, rect in enumerate(botones_cartas):
                    if rect.collidepoint(mouse_x, mouse_y):
                        # Acción al hacer clic en la carta (por ejemplo, imprimir el nombre)
                        print(f"Clic en la carta: {mano[i].get('nombre', 'Desconocida')}")

        # Rellenar la pantalla con color blanco
        screen.fill((255, 255, 255))

        # Mostrar las imágenes de las cartas
        for i, imagen in enumerate(cartas_imagenes):
            # Dibujar la imagen de la carta en su posición
            screen.blit(imagen, (x_offset + i * 110, y_offset))
            # Actualizar el rectángulo para que coincida con la posición en la pantalla
            botones_cartas[i].topleft = (x_offset + i * 110, y_offset)

        # Actualizar la pantalla
        pygame.display.flip()

    # Salir de pygame
    pygame.quit()

    
def cancelar_busqueda():
    global buscando
    buscando = False
    estado_var.set("Búsqueda cancelada")

# Crear la ventana de Tkinter
root = tk.Toplevel()
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
