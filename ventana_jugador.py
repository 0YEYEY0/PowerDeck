import Album
import tkinter as tk
from tkinter import messagebox
import Crear_Deck

# Abre la ventana del jugador
def ventana_jugador(cuenta, ventana, usuario):


    def cerrar_sesion():
        ventana_jugador.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventana_jugador = tk.Tk()
    ventana_jugador.title("Jugador")
    ventana_jugador.geometry("300x150")

    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_jugador, text="Ver Álbum", command= lambda:Album.main(usuario))
    boton_ver_album.pack(pady=10)

    #Boton para crear un mazo
    boton_crear_mazo = tk.Button(ventana_jugador, text="Crear Mazo", command= lambda:Crear_Deck.DeckManagerApp(usuario))
    boton_crear_mazo.pack(pady=10)

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_jugador, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)

