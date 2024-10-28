import json
import hashlib
import tkinter as tk
from tkinter import messagebox

def main(ventana):
    # Función para agregar un nuevo administrador
    def agregar_admin():
        with open("admin_cuenta.json", 'r') as archivo:
            data = json.load(archivo)

        if not validacion_datos(usuario.get(), contrasena.get()):
            return

        nuevo_admin = {
            "nombre_usuario": usuario.get(),
            "contraseña": hashlib.sha256(contrasena.get().encode()).hexdigest()  # Encriptar la contraseña
        }

        # Agrega el nuevo administrador a la lista de usuarios autorizados
        data['usuarios_autorizados'].append(nuevo_admin)

        # Guardar los cambios en el archivo JSON
        with open("admin_cuenta.json", 'w') as archivo:
            json.dump(data, archivo, indent=4)

        messagebox.showinfo("Finalizado", "Cuenta agregada con exito")
        ventana_crear_cuenta.destroy()
        ventana.deiconify()
        return

    def validacion_datos(usuario, contrasena):
        if not usuario or not contrasena:
            messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
            return False
        return True

    ventana.withdraw()

    ventana_crear_cuenta = tk.Tk()
    ventana_crear_cuenta.title("Creacion Cuenta Admin")
    ventana_crear_cuenta.geometry("300x200")

    label_usuario = tk.Label(ventana_crear_cuenta, text="Usuario:")
    label_usuario.pack(pady=5)
    usuario = tk.Entry(ventana_crear_cuenta)
    usuario.pack(pady=5)

    label_usuario = tk.Label(ventana_crear_cuenta, text="Contraseña:")
    label_usuario.pack(pady=5)
    contrasena = tk.Entry(ventana_crear_cuenta)
    contrasena.pack(pady=5)

    # Botón para crear cuenta admin
    boton_ver_album = tk.Button(ventana_crear_cuenta, text="Crear Cuenta", command=agregar_admin)
    boton_ver_album.pack(pady=10)

