import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Cartas'))
sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck'))
#sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Partida'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Cartas'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Partida'))
import Album as Album
import Crear_Deck as Crear_Deck
import Partida.Partida as Partida
import Matchmaking

# Abre la ventana del jugador
def ventana_jugador(cuenta, ventana, usuario):


    def cerrar_sesion():
        ventana_jugador.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventana_jugador = tk.Tk()
    ventana_jugador.title("Jugador")
    ventana_jugador.geometry("300x280")

    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_jugador, text="Ver Álbum", command=lambda: Album.main(usuario))
    boton_ver_album.pack(pady=10)

    #Boton para crear un mazo
    boton_crear_mazo = tk.Button(ventana_jugador, text="Crear Mazo", command= lambda:Crear_Deck.DeckManagerApp(usuario))
    boton_crear_mazo.pack(pady=10)

    boton_buscar_partida = tk.Button(ventana_jugador, text="Buscar Partida", command=lambda:Matchmaking.main(usuario))
    boton_buscar_partida.pack(pady=10)

    boton_jugar_bot = tk.Button(ventana_jugador, text="Jugar bot", command=lambda:Partida.partida(usuario))
    boton_jugar_bot.pack(pady=10)

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_jugador, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)

