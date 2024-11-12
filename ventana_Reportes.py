import tkinter as tk
import fileReader
import reportes

# Abre la ventana del administrador
def ver():
    # Interfaz
    ventana_reportes = tk.Tk()
    ventana_reportes.title("reportes")
    ventana_reportes.geometry("300x200")

    # Cantidad de jugadores registrados
    label_info = tk.Label(ventana_reportes, text="jugadores registrados: " + str(reportes.jugadores_registrados()))
    label_info.pack()


    # info
    label_info = tk.Label(ventana_reportes, text="info:")
    label_info.pack(pady=5)
    info_data = tk.Label(ventana_reportes, text=str(fileReader.cardAttribute("nombre", fileReader.read())))
    info_data.pack(pady=5)

