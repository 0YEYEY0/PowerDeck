import tkinter as tk
import funciones_login
from tkinter import messagebox

def main(ventana_login):
    respuesta = messagebox.askquestion("Tipo de cuenta", "¿Es una cuenta de adminsitrador?")
    print(respuesta)
    if respuesta == "yes":
        crear_admin(ventana_login)
    else:
        crear_jugador(ventana_login)


def crear_admin(ventana_login):
    ventana = tk.Tk()
    ventana.title("Crear Cuenta")
    ventana.geometry("300x270")

    # Correo
    label_correo = tk.Label(ventana, text="Correo:")
    label_correo.pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)

    # Contraseña
    label_contraseña = tk.Label(ventana, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack(pady=5)

    # Check tipo admin
    label_tipo = tk.Label(ventana, text="Tipo de administrador:")
    label_tipo.pack(pady=5)

    opcion = tk.StringVar(value="")  # Define un valor inicial (opcional)

    opcion_reporte = tk.Radiobutton(ventana, text="Reportes", variable=opcion, value="Reportes")
    opcion_reporte.pack()

    opcion_general = tk.Radiobutton(ventana, text="General", variable=opcion, value="General")
    opcion_general.pack()

    # Botón para crear cuenta
    boton_crear = tk.Button(ventana, text="Crear", command=lambda: prueba(opcion.get()))
    boton_crear.pack(pady=20)

def prueba(text):
    if text:  # Verifica si text tiene un valor
        print("Tipo seleccionado:", text)
    else:
        print("Ninguna opción seleccionada")
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
