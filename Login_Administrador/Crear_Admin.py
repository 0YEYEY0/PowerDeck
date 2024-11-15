import json
import hashlib
import tkinter as tk
from tkinter import messagebox

def main(ventana):
    # Función para agregar un nuevo administrador

    def agregar_admin():
        with open("admin_cuenta.json", 'r') as archivo:
            data = json.load(archivo)

        if not validacion_datos(usuario.get(), correo.get(), contrasena.get()):
            return
        if (var_tipo.get() == "Usuario configuracion"):
            es_usuario_configuracion = True
            es_usuario_reportes = False
        else:
            es_usuario_configuracion = False
            es_usuario_reportes = True

        nuevo_admin = {
            "nombre_usuario": usuario.get(),
            "correo": correo.get(),
            "contraseña": hashlib.sha256(contrasena.get().encode()).hexdigest(),  # Encriptar la contraseña
            "es_usuario_configuracion":  es_usuario_configuracion,
            "es_usuario_reportes": es_usuario_reportes,
            "principal": False
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

    def validacion_datos(usuario, correo, contrasena):
        if not usuario or not correo or not contrasena:
            messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
            return False
        return True

    ventana.withdraw()

    ventana_crear_cuenta = tk.Tk()
    ventana_crear_cuenta.title("Creacion Cuenta Admin")
    ventana_crear_cuenta.geometry("300x300")

    label_usuario = tk.Label(ventana_crear_cuenta, text="Usuario:")
    label_usuario.pack(pady=5)
    usuario = tk.Entry(ventana_crear_cuenta)
    usuario.pack(pady=5)

    label_correo = tk.Label(ventana_crear_cuenta, text="Correo:")
    label_correo.pack(pady=5)
    correo = tk.Entry(ventana_crear_cuenta)
    correo.pack(pady=5)

    label_usuario = tk.Label(ventana_crear_cuenta, text="Contraseña:")
    label_usuario.pack(pady=5)
    contrasena = tk.Entry(ventana_crear_cuenta)
    contrasena.pack(pady=5)

    # Check tipos de admin
    var_tipo = tk.StringVar(value="Usuario configuracion")
 
    label_tipo = tk.Label(ventana_crear_cuenta, text="Tipo de Cuenta:")
    label_tipo.pack(pady=5)
    radio_usuario_configuracion = tk.Radiobutton(ventana_crear_cuenta, text="Usuario configuracion", value="Usuario configuracion")
    radio_usuario_reportes = tk.Radiobutton(ventana_crear_cuenta, text="Usuario reportes", value="Usuario reportes")
    radio_usuario_configuracion.pack()
    radio_usuario_reportes.pack()


    # Botón para crear cuenta admin
    boton_ver_album = tk.Button(ventana_crear_cuenta, text="Crear Cuenta", command=agregar_admin)
    boton_ver_album.pack(pady=10)

