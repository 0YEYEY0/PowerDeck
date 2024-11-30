import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Cartas'))
sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Administrador'))
import fileReader as fileReader
import reportes

# Abre la ventana del administrador
def ver():
    # Interfaz
    ventana_reportes = tk.Tk()
    ventana_reportes.title("reportes")
    ventana_reportes.geometry("500x500")

    # Cantidad de jugadores registrados
    label_total_registros = tk.Label(ventana_reportes, 
                                    text="Jugadores registrados: " + str(reportes.jugadores_registrados()), font=("bold"))
    label_total_registros.pack(side = tk.TOP)

    # Cantidad de veces las cartas fueron usadas
    label_titulo_uso_cartas = tk.Label(ventana_reportes, text="Uso de cartas:", font=("bold"))
    label_titulo_uso_cartas.pack(side = tk.TOP)

    total_cartas = len([element for element in list(fileReader.read()) if isinstance(element, dict)])
    nombre_carta = fileReader.cardAttribute("nombre", fileReader.read())
    for i in range(total_cartas):
        if (fileReader.cardAttribute("es_principal", fileReader.read())[i]):
            label_usos_cartas = tk.Label(ventana_reportes, 
                                        text= str(nombre_carta[i]) + ": " + str(reportes.uso_carta(str(nombre_carta[i]), True)))
            label_usos_cartas.pack(side = tk.TOP)
        else:
            label_usos_cartas = tk.Label(ventana_reportes,
                                        text= str(nombre_carta[i]) + "(variante)" ": " + str(reportes.uso_carta(str(nombre_carta[i]), False)))
            label_usos_cartas.pack(side = tk.TOP)
 
