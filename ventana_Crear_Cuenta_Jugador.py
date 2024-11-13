import tkinter as tk

def ventana_crear_cuenta(ventana_login):
    ventana = tk.Tk()
    ventana.title("Crear Cuenta")
    ventana.geometry("300x380")
    # Nombre de usuario
    label_usuario = tk.Label(ventana, text="Nombre de usuario:")
    label_usuario.pack(pady=5)
    entry_usuario = tk.Entry(ventana)
    entry_usuario.pack(pady=5)
    # Contraseña
    label_contraseña = tk.Label(ventana, text="Contraseña:")
    label_contraseña.pack(pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.pack(pady=5)
    # Correo
    label_correo = tk.Label(ventana, text="Correo:")
    label_correo.pack(pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.pack(pady=5)
    # Nombre de la persona
    label_nombre = tk.Label(ventana, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack(pady=5)
    # País
    label_pais = tk.Label(ventana, text="País:")
    label_pais.pack(pady=5)
    entry_pais = tk.Entry(ventana)
    entry_pais.pack(pady=5)
    # Botón para crear cuenta
    boton_crear = tk.Button(ventana, text="Crear")
    boton_crear.pack(pady=20)
    ventana.mainloop()