import json
import random
import hashlib
import ventana_administrador
import ventana_jugador
import tkinter as tk
from tkinter import messagebox


# Carga las cartas desde un archivo JSON
def cargar_cartas(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)


# Asigna cartas aleatorias a un jugador
def asignar_cartas(cartas_disponibles, cantidad=5):
    if len(cartas_disponibles) < cantidad:
        return cartas_disponibles  # Si hay menos de 20 cartas, asigna todas las disponibles

    # Define las probabilidades según la rareza
    probabilidades = {
        "Ultra-Rara": 0.05,
        "Muy Rara": 0.12,
        "Rara": 0.18,
        "Normal": 0.25,
        "Básica": 0.40
    }

    # Crear una lista de cartas con probabilidades
    cartas_con_probabilidades = []
    for carta in cartas_disponibles:
        rareza = carta.get("tipo_carta", "basica")  # Asume "basica" si no se especifica la rareza
        probabilidad = probabilidades.get(rareza, 0.40)  # Asume 40% si la rareza no está en el diccionario
        cartas_con_probabilidades.extend([carta] * int(probabilidad * 100))

    # Seleccionar cartas aleatorias basadas en las probabilidades
    return random.sample(cartas_con_probabilidades, cantidad)


# Crea una cuenta de usuario
def crear_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais, es_administrador, cartas_disponibles):
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()  # Cifra la contraseña

    cuenta = {
        "nombre_usuario": nombre_usuario,
        "contraseña": hash_contraseña,
        "correo": correo,
        "nombre_persona": nombre_persona,
        "pais": pais,
        "es_administrador": es_administrador,
        "cartas": []
    }
    if not es_administrador:
        cuenta["cartas"] = asignar_cartas(cartas_disponibles, cantidad=5)
    return cuenta


# Guarda la cuenta en un archivo JSON
def guardar_cuenta(cuenta, ruta_archivo):
    with open(ruta_archivo, 'w') as archivo:
        json.dump(cuenta, archivo, indent=4)


# Valida que se haya ingresado todos los datos
def validacion_de_datos(nombre_usuario, contraseña, correo, nombre_persona, pais):
    if not nombre_usuario or not contraseña or not correo or not nombre_persona or not pais:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
        return False
    return True


# Verifica si las credenciales son válidas para crear una cuenta de administrador
def validar_admin(nombre_usuario, contraseña):
    try:
        with open("admin_cuenta.json", 'r') as archivo:
            admin_data = json.load(archivo)
            for usuario in admin_data["usuarios_autorizados"]:
                if usuario["nombre_usuario"] == nombre_usuario and usuario["contraseña"] == hashlib.sha256(contraseña.encode()).hexdigest():
                    return True
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de administrador no encontrado.")
    return False


# Verifica si la cuenta ya existe
def cuenta_existente(nombre_usuario):
    try:
        with open(f"{nombre_usuario}_cuenta.json", 'r') as archivo:
            return True  # La cuenta ya existe
    except FileNotFoundError:
        return False  # La cuenta no existe


# Procesa la creación de cuenta desde la interfaz
def procesar_creacion_cuenta():
    nombre_usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    correo = entry_correo.get()
    nombre_persona = entry_nombre.get()
    pais = entry_pais.get()
    es_administrador = var_tipo.get() == "Administrador"

    # Validación de datos
    if not validacion_de_datos(nombre_usuario, contraseña, correo, nombre_persona, pais):
        return  # Detener si la validación falla

    # Verificar si la cuenta ya existe
    if cuenta_existente(nombre_usuario):
        messagebox.showerror("Error", "La cuenta ya está creada.")
        return

    # Si es administrador, validar credenciales
    if es_administrador:
        if not validar_admin(nombre_usuario, contraseña):
            messagebox.showerror("Error", "Credenciales de administrador no válidas.")
            return

    cartas_disponibles = []

    # Carga las cartas en cartas_disponibles desde el archivo json
    if not es_administrador:
        try:
            cartas_disponibles = cargar_cartas("cartas.json")
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo de cartas no encontrado.")
            return

    cuenta = crear_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais, es_administrador, cartas_disponibles)
    ruta_guardado = f"{nombre_usuario}_cuenta.json"
    guardar_cuenta(cuenta, ruta_guardado)
    messagebox.showinfo("Cuenta Creada", "Cuenta creada con éxito.")

    # Vaciar todos los campos después de crear la cuenta
    entry_usuario.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_pais.delete(0, tk.END)



# Verifica los datos para iniciar sesión
def procesar_inicio_sesion():
    nombre_usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    correo = entry_correo.get()
    nombre_persona = entry_nombre.get()
    pais = entry_pais.get()

    # Validación de datos
    if not validacion_de_datos(nombre_usuario, contraseña, correo, nombre_persona, pais):
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

    # Verifica que todos los datos coincidan
    if (cuenta["contraseña"] == hash_contraseña and
            cuenta["correo"] == correo and
            cuenta["nombre_persona"] == nombre_persona and
            cuenta["pais"] == pais):

        messagebox.showinfo("Inicio de Sesión Exitoso", f"¡Bienvenido {nombre_usuario}!")

        # Vaciar todos los campos después de iniciar sesion
        entry_usuario.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_pais.delete(0, tk.END)

        if cuenta["es_administrador"]:
            ventana_administrador.ventana_administrador(ventana)
        else:
            ventana_jugador.ventana_jugador(cuenta, ventana, ruta_cuenta)
    else:
        messagebox.showerror("Error", "Uno o más datos son incorrectos.")


# Interfaz
ventana = tk.Tk()
ventana.title("Sistema de Cuenta")
ventana.geometry("300x450")

# Nombre de usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)

# Contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

# Nombre de la persona
label_nombre = tk.Label(ventana, text="Nombre de la persona:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Correo
label_correo = tk.Label(ventana, text="Correo:")
label_correo.pack(pady=5)
entry_correo = tk.Entry(ventana)
entry_correo.pack(pady=5)

# País
label_pais = tk.Label(ventana, text="País:")
label_pais.pack(pady=5)
entry_pais = tk.Entry(ventana)
entry_pais.pack(pady=5)

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