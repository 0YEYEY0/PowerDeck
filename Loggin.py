import json
import random
import hashlib
<<<<<<< HEAD
=======
import Album
>>>>>>> origin/Crear_Cuenta
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
<<<<<<< HEAD
def crear_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais, es_administrador, cartas_disponibles):
=======
def crear_cuenta(nombre_usuario, contraseña, es_administrador, cartas_disponibles):
>>>>>>> origin/Crear_Cuenta
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()  # Cifra la contraseña

    cuenta = {
        "nombre_usuario": nombre_usuario,
        "contraseña": hash_contraseña,
<<<<<<< HEAD
        "correo": correo,
        "nombre_persona": nombre_persona,
        "pais": pais,
=======
>>>>>>> origin/Crear_Cuenta
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


<<<<<<< HEAD
# Valida que se haya ingresado todos los datos
def validacion_de_datos(nombre_usuario, contraseña, correo, nombre_persona, pais):
    if not nombre_usuario or not contraseña or not correo or not nombre_persona or not pais:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos solicitados.")
        return False
    return True


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

    # Carga las cartas en cartas_disponible desde el archivo json
=======
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
>>>>>>> origin/Crear_Cuenta
    try:
        cartas_disponibles = cargar_cartas("cartas.json")
    except FileNotFoundError:
        messagebox.showerror("Error", "Archivo de cartas no encontrado.")
        return

<<<<<<< HEAD
    cuenta = crear_cuenta(nombre_usuario, contraseña, correo, nombre_persona, pais, es_administrador, cartas_disponibles)
=======
    cuenta = crear_cuenta(nombre_usuario, contraseña, es_administrador, cartas_disponibles)
>>>>>>> origin/Crear_Cuenta
    ruta_guardado = f"{nombre_usuario}_cuenta.json"
    guardar_cuenta(cuenta, ruta_guardado)
    messagebox.showinfo("Cuenta Creada", "Cuenta creada con éxito.")

<<<<<<< HEAD
    # Vaciar todos los campos después de crear la cuenta
    entry_usuario.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_pais.delete(0, tk.END)
=======
    entry_nombre.delete(0, tk.END)
    entry_contraseña.delete(0, tk.END)
>>>>>>> origin/Crear_Cuenta


# Abre la ventana del administrador
def abrir_ventana_administrador():
    ventana_admin = tk.Toplevel(ventana)
    ventana_admin.title("Administrador")
    ventana_admin.geometry("300x150")

    # Botón para ver álbum
<<<<<<< HEAD
    boton_ver_album = tk.Button(ventana_admin, text="Ver Álbum", command=lambda: None)
=======
    boton_ver_album = tk.Button(ventana_admin, text="Ver Álbum", command= Album.main)
>>>>>>> origin/Crear_Cuenta
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

<<<<<<< HEAD
    # Mostrar las cartas asignadas al jugador (opcional)
    messagebox.showinfo("Cartas Asignadas", f"Cartas asignadas:\n\n{cuenta['cartas']}")


# Verifica los datos para iniciar sesión
def procesar_inicio_sesion():
    nombre_usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    # Validación de datos
    if not validacion_de_datos(nombre_usuario, contraseña, None, None, None):
        return  # Detener si la validación falla
=======


# Verifica el nombre de usuario y contraseña para inciar sesión
def procesar_inicio_sesion():
    nombre_usuario = entry_nombre.get()
    contraseña = entry_contraseña.get()

    # Valida que se haya ingresado el nombre y la contraseña
    if not nombre_usuario or not contraseña:
        messagebox.showerror("Error", "Por favor, ingresa un nombre de usuario y una contraseña.")
        return
>>>>>>> origin/Crear_Cuenta

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
<<<<<<< HEAD
ventana.geometry("300x450")

# Nombre de usuario
label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack(pady=5)
=======
ventana.geometry("300x300")

# Nombre de usuario
label_nombre = tk.Label(ventana, text="Nombre de Usuario:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)
>>>>>>> origin/Crear_Cuenta

# Contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack(pady=5)

<<<<<<< HEAD
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

=======
>>>>>>> origin/Crear_Cuenta
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
