import json
import random
import hashlib
import Album
import tkinter as tk
from tkinter import messagebox


# Carga las cartas desde un archivo JSON
def cargar_cartas(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)


# Asigna cartas aleatorias a un jugador
def asignar_cartas(cartas_disponibles, cantidad=20):
    if len(cartas_disponibles) < cantidad:
        return cartas_disponibles  # Si hay menos de 20 cartas, asignar todas las disponibles
    return random.sample(cartas_disponibles, cantidad)


# Crea una cuenta de usuario
def crear_cuenta(nombre_usuario, contraseña, es_administrador, cartas_disponibles):
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()  # Cifra la contraseña

    cuenta = {
        "nombre_usuario": nombre_usuario,
        "contraseña": hash_contraseña,
        "es_administrador": es_administrador,
        "cartas": []
    }
    if not es_administrador:
        cuenta["cartas"] = asignar_cartas(cartas_disponibles, cantidad=20)
    return cuenta


# Guarda la cuenta en un archivo JSON
def guardar_cuenta(cuenta, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(cuenta, archivo, indent=4)


# Procesa la creación de cuenta desde la interfaz
def procesar_creacion_cuenta():
    nombre_usuario = entry_nombre.get()
    contraseña = entry_contraseña.get()
    es_administrador = var_tipo.get() == "Administrador"

    # Validacioón de datos
    if not nombre_usuario or not contraseña:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    # Carga las cartas en cartas_disponible desde el archuvo json
    try:
        cartas_disponibles = cargar_cartas("cartas.json")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de cartas no encontrado.")
        return

    cuenta = crear_cuenta(nombre_usuario, contraseña, es_administrador, cartas_disponibles)
    ruta_guardado = f"{nombre_usuario}_cuenta.json"
    guardar_cuenta(cuenta, ruta_guardado)
    messagebox.showinfo("Cuenta Creada", "Cuenta creada con éxito.")

    entry_nombre.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)


# Abre la ventana del administrador
def abrir_ventana_administrador():
    ventana_admin = tk.Toplevel(ventana)
    ventana_admin.title("Administrador")
    ventana_admin.geometry("300x150")

    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_admin, text="Ver Álbum", command= Album.main)
    boton_ver_album.pack(pady=10)

    # Botón para crear carta
    boton_crear_carta = tk.Button(ventana_admin, text="Crear Carta", command=lambda: None)
    boton_crear_carta.pack(pady=10)


# Abre la ventana del jugador
def abrir_ventana_jugador(cuenta):
    ventana_jugador = tk.Toplevel(ventana)
    ventana_jugador.title("Jugador")
    ventana_jugador.geometry("300x100")

    # Botón para ver álbum
    boton_ver_album = tk.Button(ventana_jugador, text="Ver Álbum", command=lambda: None)
    boton_ver_album.pack(pady=10)



# Verifica el nombre de usuario y contraseña para inciar sesión
def procesar_inicio_sesion():
    nombre_usuario = entry_nombre.get()
    contraseña = entry_contraseña.get()

    # Valida que se haya ingresado el nombre y la contraseña
    if not nombre_usuario or not contraseña:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return

    ruta_cuenta = f"{nombre_usuario}_cuenta.json"
    try:
        with open(ruta_cuenta, 'r') as archivo:
            cuenta = json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "Cuenta no encontrada.")
        return

    # Cifra la contraseña y la compara con la guardada
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    if cuenta["contraseña"] == hash_contraseña:
        messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido {nombre_usuario}!")
        if cuenta["es_administrador"]:
            abrir_ventana_administrador()
        else:
            abrir_ventana_jugador(cuenta)
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")


# Interfaz
ventana = tk.Tk()
ventana.title("Sistema de Cuenta")
ventana.geometry("300x300")

# Nombre de usuario
label_nombre = tk.Label(ventana, text="Nombre de Usuario:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

# Check jugador-admin
var_tipo = tk.StringVar(value="Jugador")
label_tipo = tk.Label(ventana, text="Tipo de Cuenta:")
label_tipo.pack(pady=5)
radio_jugador = tk.Radiobutton(ventana, text="Jugador", variable=var_tipo, value="Jugador")
radio_administrador = tk.Radiobutton(ventana, text="Administrador", variable=var_tipo, value="Administrador")
radio_jugador.pack()
radio_administrador.pack()

# Botón para crear la cuenta
boton_crear = tk.Button(ventana, text="Crear Cuenta", command=procesar_creacion_cuenta)
boton_crear.pack(pady=5)

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=procesar_inicio_sesion)
boton_iniciar_sesion.pack(pady=5)

ventana.mainloop()
