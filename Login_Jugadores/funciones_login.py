import json
import hashlib
import random
import sys
import os
sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Login_Jugadores/Ventanas'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Jugadores/Ventanas'))
sys.path.append(os.path.abspath('C:/Users/menei/Documents/GitHub/PowerDeck/PowerDeck/Cartas'))
import Ventanas.Ventana_Jugador as ventana_jugador
import cartas as id
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
    if not (4 <= len(contraseña) <= 6) or not contraseña.isalnum():
        messagebox.showerror("Error", "La contraseña debe ser alfanumérica y contener de 4 a 6 caracteres.")
        return False
    return True

def procesar_inicio_sesion(contraseña, correo):
    if not validacion_inicio_sesion(contraseña, correo):
        return False

    ruta_cuenta = "Jugadores/" + f"{correo}_cuenta.json"
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

def cuenta_existente(nombre_usuario):
    try:
        with open("Jugadores/"+f"{nombre_usuario}_cuenta.json", 'r') as archivo:
            return True
    except FileNotFoundError:
        return False
    
def correo_existente(correo):
    try:
        with open("Jugadores/correos.json", 'r') as archivo:
            correos = json.load(archivo)
            return correo in correos
    except FileNotFoundError:
        return False
    
def iniciar_sesion(correo, contraseña, ventana, entry_contraseña, entry_correo):
    cuenta = procesar_inicio_sesion(contraseña, correo)
    ruta_cuenta = "Jugadores/" + f"{correo}_cuenta.json"
    if cuenta:
        entry_correo.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)
        ventana.withdraw()
        messagebox.showinfo("Inicio de Sesión Exitoso", "¡Bienvenido!")

        ventana_jugador.ventana_jugador(cuenta, ventana, ruta_cuenta)
    else:
        messagebox.showerror("Error", "Uno o más datos son incorrectos.")

def cargar_cartas(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

def asignar_cartas(cartas_disponibles, cantidad):
    if len(cartas_disponibles) < cantidad:
        return cartas_disponibles  # Si hay menos de 20 cartas, asigna todas las disponibles

    # Define las probabilidades según la rareza
    probabilidades = {
        "Ultra-Rara": 0.05,
        "Muy-Rara": 0.12,
        "Rara": 0.18,
        "Normal": 0.25,
        "Basica": 0.40
    }

    # Crear una lista de cartas con probabilidades
    cartas_con_probabilidades = []
    for carta in cartas_disponibles:
        rareza = carta.get("tipo_carta", "basica")  # Asume "basica" si no se especifica la rareza
        probabilidad = probabilidades.get(rareza, 0.40)  # Asume 40% si la rareza no está en el diccionario
        cartas_con_probabilidades.extend([carta] * int(probabilidad * 100))

    # Seleccionar cartas aleatorias basadas en las probabilidades sin repetir nombres a menos que tengan variantes
    cartas_asignadas = []
    nombres_asignados = set()
    while len(cartas_asignadas) < cantidad:
        carta_seleccionada = random.choice(cartas_con_probabilidades)
        nombre_carta = carta_seleccionada["nombre"]
        variante_carta = carta_seleccionada.get("variante", "")

        if (nombre_carta, variante_carta) not in nombres_asignados:
            cartas_asignadas.append(carta_seleccionada)
            nombres_asignados.add((nombre_carta, variante_carta))

    # Mostrar mensaje con las cartas asignadas
    nombres_cartas_asignadas = [carta["nombre"] for carta in cartas_asignadas]
    messagebox.showinfo("Cartas Asignadas", f"Se te han asignado las siguientes cartas: {', '.join(nombres_cartas_asignadas)}")

    return cartas_asignadas

def crear_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais):
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()  # Cifra la contraseña

    cuenta = {
        "id": id.generar_id_unico(),
        "nombre_usuario": nombre_usuario,
        "contraseña": hash_contraseña,
        "correo": correo,
        "nombre_persona": nombre_persona,
        "pais": pais,
        "es_administrador": False,
        "cartas": []
    }

    cartas = cargar_cartas("Cartas/cartas.json")
    cuenta["cartas"] = asignar_cartas(cartas, 7)
    return cuenta

def guardar_cuenta(cuenta, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(cuenta, archivo, indent=4)

def guardar_correo(correo, ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            correos = json.load(archivo)
    except FileNotFoundError:
        correos = []

    correos.append(correo)

    with open(ruta_archivo, 'w') as archivo:
        json.dump(correos, archivo, indent=4)

def procesar_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais, ventana):

    # Validación de datos
    if not validacion_creacion_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais):
        return  # Detener si la validación falla
    # Verificar si la cuenta ya existe
    if cuenta_existente(nombre_usuario):
        messagebox.showerror("Error", "Ya existe este nombre de usuario.")
        return
    
    #Verificar que el correo sea unico
    if correo_existente(correo):
        messagebox.showerror("Error", "Este correo ya esta asociado a otro nombre de usuario.")
        return

    # Carga las cartas en cartas_disponibles desde el archivo json
    try:
        cartas_disponibles = cargar_cartas("Cartas/cartas.json")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de cartas no encontrado.")
        return

    cuenta = crear_cuenta_jugador(nombre_usuario, contraseña, correo, nombre_persona, pais)
    ruta_guardado = "Jugadores/"+f"{correo}_cuenta.json"
    guardar_cuenta(cuenta, ruta_guardado)
    guardar_correo(correo, "Jugadores/correos.json")
    messagebox.showinfo("Cuenta Creada", "Cuenta creada con éxito.")

    ventana.destroy()


