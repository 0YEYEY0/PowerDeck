import tkinter as tk
import funciones_login
import interfaz_crear_cuenta

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
boton_crear_cuenta = tk.Button(ventana, text="Crear Cuenta", command=lambda: interfaz_crear_cuenta.main(ventana))
boton_crear_cuenta.pack(pady=5)

ventana.mainloop()
