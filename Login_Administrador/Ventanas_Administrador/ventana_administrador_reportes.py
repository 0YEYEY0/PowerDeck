import tkinter as tk
import Login_Administrador.Ventanas_Administrador.ventana_Reportes as ventana_Reportes
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

    # Botón para cerrar sesion
    boton_cerrar_sesion = tk.Button(ventana_admin, text="Cerrar Sesion", command=cerrar_sesion)
    boton_cerrar_sesion.pack(pady=10)
