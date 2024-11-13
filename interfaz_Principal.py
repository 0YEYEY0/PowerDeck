import tkinter as tk
import ventana_Crear_Cuenta_Jugador

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
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión")
boton_iniciar_sesion.pack(pady=5)
# Botón para crear cuenta
boton_crear_cuenta = tk.Button(ventana, text="Crear Cuenta", command=lambda: ventana_Crear_Cuenta_Jugador.ventana_crear_cuenta(ventana))
boton_crear_cuenta.pack(pady=5)
ventana.mainloop()


