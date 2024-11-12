import tkinter as tk
import fileReader
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

    cardsTotal = len([element for element in list(fileReader.read()) if isinstance(element, dict)])

    for i in range(cardsTotal):
        if (fileReader.cardAttribute("es_principal", fileReader.read())[i]):
            label_usos_cartas = tk.Label(ventana_reportes, 
                                        text= str(fileReader.cardAttribute("nombre", fileReader.read())[i]) + ": " + str(i))
            label_usos_cartas.pack(side = tk.TOP)
        else:
            label_usos_cartas = tk.Label(ventana_reportes,
                                        text= str(fileReader.cardAttribute("nombre", fileReader.read())[i]) + "(variante)" ": " + str(i))
            label_usos_cartas.pack(side = tk.TOP)
 
