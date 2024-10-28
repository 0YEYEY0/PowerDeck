import Album
import tkinter as tk
from tkinter import messagebox

# Abre la ventana del jugador
def ventana_jugador(cuenta, ventana):


    def cerrar_sesion():
        ventana_jugador.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventana_jugador = tk.Tk()
    ventana_jugador.title("Jugador")
    ventana_jugador.geometry("300x100")

    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_jugador, text="Ver Álbum", command= Album.main)
    boton_ver_album.pack(pady=10)

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_jugador, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)

    # Mostrar las cartas asignadas al jugador (opcional)
    messagebox.showinfo("Cartas Asignadas", f"Cartas asignadas:\n\n{cuenta['cartas']}")
