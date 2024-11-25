import tkinter as tk
import sys
import os
#sys.path.append(os.path.abspath('C:/Users/menei/Documents/Github/PowerDeck/Login_Jugadores'))
sys.path.append(os.path.abspath("C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Login_Jugadores"))

import Login_Jugadores.funciones_login as funciones_login
from tkinter import messagebox

def main(ventana_login):
   crear_jugador(ventana_login)
# Interfaz de creación de cuenta
def crear_jugador(ventana_login):
   ventana = tk.Toplevel()
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
   lista_paises = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Barbuda", "Argentina", "Armenia", 
                  "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", 
                  "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
                  "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Capo Verde", "Central African Republic", "Chad", 
                  "Chile","China", "Colombia", "Comoros", "Congo(Republic)", "Congo {Democratic Republic}","Costa Rica", "Côte dIvoire","Croatia", 
                  "Cuba","Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica","Dominican Republic", 
                  "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea","Eritrea", "Estonia","Ethiopia", "Eswatini",
                  "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", 
                  "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India",
                  "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan","Jordan", 
                  "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan",
                  "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
                  "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", 
                  "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", 
                  "Morocco", "Mozambique", "Myanmar(Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", 
                  "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
                  "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", 
                  "Rwanda", "St Kitts & Nevis", "St Lucia", "St Vincent & the Grenadines", "Samoa", "San Marino", 
                  "Sao Tome & Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
                  "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
                  "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", 
                  "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", 
                  "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", 
                  "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
   label_pais = tk.Label(ventana, text="País:")
   label_pais.pack(pady=5)

   pais_seleccionado = tk.StringVar()
   pais_seleccionado.set(lista_paises[0])

   caja_pais = tk.OptionMenu(ventana,pais_seleccionado, *lista_paises)
   caja_pais.pack()


   # Botón para crear cuenta
   boton_crear = tk.Button(ventana, text="Crear", command=lambda: funciones_login.procesar_cuenta_jugador(entry_usuario.get(), entry_contraseña.get(), entry_correo.get(),
                                                                                                         entry_nombre.get(), pais_seleccionado.get(), ventana))
   boton_crear.pack(pady=20)

   ventana.mainloop()
    
