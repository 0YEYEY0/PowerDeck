import tkinter as tk
import fileReader

# Abre la ventana del administrador
def ver():
    # Interfaz
    ventana_reportes = tk.Tk()
    ventana_reportes.title("reportes")
    ventana_reportes.geometry("300x200")
    
    # info
    label_info = tk.Label(ventana_reportes, text="info:")
    label_info.pack(pady=5)
    info_data = tk.Label(ventana_reportes, text=str(fileReader.cardAttribute("nombre", fileReader.read())))
    info_data.pack(pady=5)