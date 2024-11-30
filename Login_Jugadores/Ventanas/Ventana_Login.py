import tkinter as tk
import sys
import os

#sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Login_Jugadores/Ventanas'))
#sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Login_Jugadores'))
sys.path.append(os.path.abspath("C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Jugadores/Ventanas"))
sys.path.append(os.path.abspath("C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Jugadores"))
import funciones_login as funciones_login
import Ventana_Crear_Cuenta as Ventana_Crear_Cuenta


# Interfaz de inicio de sesión
ventana = tk.Tk()
ventana.title("Iniciar Sesión")
ventana.geometry("300x200")

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
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=lambda: funciones_login.iniciar_sesion(entry_correo.get(), entry_contraseña.get(), ventana, entry_contraseña, entry_correo))
boton_iniciar_sesion.pack(pady=5)

# Botón para crear cuenta
boton_crear_cuenta = tk.Button(ventana, text="Crear Cuenta", command=lambda: Ventana_Crear_Cuenta.main(ventana))
boton_crear_cuenta.pack(pady=5)


ventana.mainloop()
