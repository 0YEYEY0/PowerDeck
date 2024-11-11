import tkinter as tk
import Album
import interfaz
# Abre la ventana del administrador
def ventana_administrador_configuracion(ventana):

    def cerrar_sesion():
        ventana_admin.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventana_admin = tk.Tk()
    ventana_admin.title("Usuario de configuración")
    ventana_admin.geometry("300x200")
    
    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_admin, text="Ver Álbum", command= Album.main)
    boton_ver_album.pack(pady=10)

    # Botón para crear carta
    boton_crear_carta = tk.Button(ventana_admin, text="Crear Carta", command= interfaz.main)
    boton_crear_carta.pack(pady=10)

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_admin, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)

