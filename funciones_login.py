import json
import hashlib
import random
import ventana_jugador
import ventana_administrador
import tkinter as tk
from tkinter import messagebox

# Valida que se haya ingresado todos los datos
def validacion_inicio_sesion(contraseña, correo):
    if not correo or not contraseña:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
        return False
    return True

def validacion_creacion_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais):
    if not nombre_usuario or not contraseña or not correo or not nombre_persona or not pais:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
        return False
    return True
def procesar_inicio_sesion(contraseña, correo):
    if not validacion_inicio_sesion(contraseña, correo):
        return False

    ruta_cuenta = f"{correo}_cuenta.json"
    try:
        with open(ruta_cuenta, 'r') as archivo:
            cuenta = json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "Cuenta no encontrada.")
        return False

    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    if cuenta.get("contraseña") == hash_contraseña and cuenta.get("correo") == correo:
        return cuenta
    else:
        messagebox.showerror("Error", "Uno o más datos son incorrectos.")
        return False

# Verifica si las credenciales son válidas para crear una cuenta de administrador
def validar_admin(nombre_usuario, contraseña):
    try:
        with open("admin_cuenta.json", 'r') as archivo:
            admin_data = json.load(archivo)
            for usuario in admin_data["usuarios_autorizados"]:
                if usuario["nombre_usuario"] == nombre_usuario and usuario["contraseña"] == hashlib.sha256(
                        contraseña.encode()).hexdigest():
                    return True
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de administrador no encontrado.")
    return False

def cuenta_existente(nombre_usuario):
    try:
        with open(f"{nombre_usuario}_cuenta.json", 'r') as archivo:
            return True
    except FileNotFoundError:
        return False
def iniciar_sesion(correo, contraseña, ventana, entry_contraseña, entry_correo):
    cuenta = procesar_inicio_sesion(contraseña, correo)
    if cuenta:
        entry_correo.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)
        ventana.withdraw()
        messagebox.showinfo("Inicio de Sesión Exitoso", "¡Bienvenido!")

        if cuenta["es_administrador"]:
            ventana_administrador.ventana_administrador(ventana)
        else:
            ventana_jugador.ventana_jugador(ventana)
    else:
        messagebox.showerror("Error", "Uno o más datos son incorrectos.")

def cargar_cartas(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

# Asigna cartas aleatorias a un jugador
def asignar_cartas(cartas_disponibles, cantidad):
    if len(cartas_disponibles) < cantidad:
        return cartas_disponibles  # Si hay menos de 20 cartas, asigna  todas las disponibles
    return random.sample(cartas_disponibles, cantidad)

def crear_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais):
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()  # Cifra la contraseña

    cuenta = {
        "nombre_usuario": nombre_usuario,
        "contraseña": hash_contraseña,
        "correo": correo,
        "nombre_persona": nombre_persona,
        "pais": pais,
        "es_administrador": False,
        "cartas": []
    }

    cartas = cargar_cartas("cartas.json")
    cuenta["cartas"] = asignar_cartas(cartas, 20)
    return cuenta

def guardar_cuenta(cuenta, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(cuenta, archivo, indent=4)

def procesar_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais, ventana):

    # Validación de datos

    if not validacion_creacion_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais):
        return  # Detener si la validación falla
    # Verificar si la cuenta ya existe
    if cuenta_existente(nombre_usuario):
        messagebox.showerror("Error", "La cuenta ya está creada.")
        return

    # Carga las cartas en cartas_disponibles desde el archivo json
    try:
        cartas_disponibles = cargar_cartas("cartas.json")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de cartas no encontrado.")
        return

    cuenta = crear_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais)
    ruta_guardado = f"{nombre_usuario}_cuenta.json"
    guardar_cuenta(cuenta, ruta_guardado)
    messagebox.showinfo("Cuenta Creada", "Cuenta creada con éxito.")

    ventana.destroy()


