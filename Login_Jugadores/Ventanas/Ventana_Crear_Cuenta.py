import tkinter as tk
import Login_Jugadores.funciones_login as funciones_login
from tkinter import messagebox

def main(ventana_login):
   crear_jugador(ventana_login)
# Interfaz de creación de cuenta
def crear_jugador(ventana_login):
    ventana = tk.Tk()
    ventana.title("Crear Cuenta")
    ventana.geometry("300x380")

    # Nombre de usuario
    label_usuario = tk.Label(ventana, text="Nombre de usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)

    # Contraseña
    label_contraseña = tk.Label(ventana, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack(pady=5)

    # Correo
    label_correo = tk.Label(ventana, text="Correo:")
    label_correo.pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    # Nombre de la persona
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)

    # País
    label_pais = tk.Label(ventana, text="País:")
    label_pais.pack(pady=5)
    entry_pais = tk.Entry(ventana)
    entry_pais.pack(pady=5)

    # Botón para crear cuenta
    boton_crear = tk.Button(ventana, text="Crear", command=lambda: funciones_login.procesar_cuenta_jugador(entry_usuario.get(), entry_contraseña.get(), entry_correo.get(),
                                                                                                           entry_nombre.get(), entry_pais.get(), ventana))
    boton_crear.pack(pady=20)

    ventana.mainloop()
    
