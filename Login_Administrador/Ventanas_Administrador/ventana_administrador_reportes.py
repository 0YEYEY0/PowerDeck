import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Administrador/Ventanas_Administrador'))
sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Administrador'))
import ventana_Reportes as ventana_Reportes
import Crear_Admin
# Abre la ventana del administrador
def ventana_administrador_reportes(ventana):

    def cerrar_sesion():
        ventana_admin.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventana_admin = tk.Tk()
    ventana_admin.title("Usuario de reportes")
    ventana_admin.geometry("300x200")

    # Botón para ver reportes
    boton_ver_reportes = tk.Button(ventana_admin, text="Ver reportes", command= ventana_Reportes.ver)
    boton_ver_reportes.pack(pady=10)

    # Botón para crear cuenta admin
    boton_crear_cuenta = tk.Button(ventana_admin, text="Crear Cuenta Administrador", command=lambda: Crear_Admin.main(ventana_admin))
    boton_crear_cuenta.pack(pady=10)

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_admin, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)
