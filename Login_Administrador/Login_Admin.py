import json
import random
import hashlib
import sys
import os
sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Login_Administrador/Ventanas_Administrador'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Administrador/Ventanas_Administrador'))

import Ventanas_Administrador.ventana_administrador as ventana_administrador
import Ventanas_Administrador.ventana_administrador_configuracion as ventana_administrador_configuracion
import Ventanas_Administrador.ventana_administrador_reportes as ventana_administrador_reportes
import tkinter as tk
from tkinter import messagebox

admin_cuenta_ruta = "Administradores/admin_cuenta.json"

# Verifica si las credenciales son válidas
def validar_admin(nombre_usuario, correo, contraseña):
    try:
        with open(admin_cuenta_ruta, 'r') as archivo:
            admin_data = json.load(archivo)
            #verifica admin padre
            if (admin_data["nombre_usuario"] == nombre_usuario and admin_data["correo"] == correo and
                    admin_data["contraseña"] == hashlib.sha256(contraseña.encode()).hexdigest()): 
                return True

            #verifica admins
            for usuario in admin_data["usuarios_autorizados"]:
                if (usuario["nombre_usuario"] == nombre_usuario and usuario["correo"] == correo and
                    usuario["contraseña"] == hashlib.sha256(contraseña.encode()).hexdigest()): 
                    return True         
    except FileNotFoundError:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
    return False

# Verifica los datos para iniciar sesión
def procesar_inicio_sesion():
    nombre_usuario = entry_usuario.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()

    # Validación de datos
    if not validar_admin(nombre_usuario, correo, contraseña):
        messagebox.showerror("Error", "Uno o más datos son incorrectos.")
        return
    try:
        #ruta_admin = f"{nombre_usuario}_cuenta.json"
        with open(admin_cuenta_ruta, 'r') as archivo:
            admin = json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "Cuenta no encontrada.")
        return

    # Cifra la contraseña y la compara con la guardada
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()

    # Verifica que todos los datos coincidan
    if (admin["contraseña"] == hash_contraseña and
            admin["correo"] == correo and
            admin["nombre_usuario"] == nombre_usuario):
        
        messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido {nombre_usuario}!")

        # Vaciar todos los campos después de iniciar sesion
        entry_usuario.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)
        entry_correo.delete(0, tk.END)

        ventana_administrador.ventana_administrador(ventana)

    else:
        for usuario in admin["usuarios_autorizados"]:
            if (usuario["contraseña"] == hash_contraseña and usuario["correo"] == correo and
                usuario["nombre_usuario"] == nombre_usuario):

                # Vaciar todos los campos después de iniciar sesion
                entry_usuario.delete(0, tk.END)
                entry_contraseña.delete(0, tk.END)
                entry_correo.delete(0, tk.END)

                messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido {nombre_usuario}!")

                if usuario["es_usuario_configuracion"]:
                    ventana_administrador_configuracion.ventana_administrador_configuracion(ventana)
                else:
                    ventana_administrador_reportes.ventana_administrador_reportes(ventana)

# Interfaz
ventana = tk.Tk()
ventana.title("Sistema de Admin")
ventana.geometry("300x450")

# Nombre de usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

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

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=procesar_inicio_sesion)
boton_iniciar_sesion.pack(pady=5)

ventana.mainloop()