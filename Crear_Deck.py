import tkinter as tk
from tkinter import messagebox, Listbox, Entry, Label
import json
from collections import Counter

# Define las restricciones de tipo de carta como porcentajes
restricciones_tipo = {
    "Ultra Rara": 0.1,  # máximo del 10%
    "Muy Rara": 0.15,   # máximo del 15%
    "Rara": 0.2,        # máximo del 20%
    "Normal": 0.6,      # máximo del 60%
    "Básica": 1.0       # máximo del 100%
}

class DeckBuilderApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Construcción de Mazo")
        self.username = username
        self.deck_size = 5

        # Cargar cartas del usuario actual y los mazos creados
        self.cargar_cartas_usuario()

        # Campo para ingresar el nombre del mazo
        self.label_nombre = Label(root, text="Nombre del Mazo:")
        self.label_nombre.pack()
        self.entry_nombre = Entry(root)
        self.entry_nombre.pack()

        # Listas para mostrar cartas y mazo
        self.lista_cartas = Listbox(root, selectmode=tk.SINGLE)
        self.lista_cartas.pack(side=tk.LEFT, padx=10, pady=10)
        self.mostrar_cartas_disponibles()

        self.lista_mazo = Listbox(root)
        self.lista_mazo.pack(side=tk.LEFT, padx=10, pady=10)

        # Botones para agregar, remover cartas y guardar el mazo
        self.boton_agregar = tk.Button(root, text="Agregar al mazo", command=self.agregar_al_mazo)
        self.boton_agregar.pack(pady=5)
        self.boton_remover = tk.Button(root, text="Remover del mazo", command=self.remover_del_mazo)
        self.boton_remover.pack(pady=5)
        self.boton_guardar = tk.Button(root, text="Guardar Mazo", command=self.guardar_mazo)
        self.boton_guardar.pack(pady=5)

    def cargar_cartas_usuario(self):
        # Cargar los datos desde el archivo JSON del usuario
        with open(f"{self.username}.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)
        self.cartas_disponibles = self.data["cartas"]
        self.mazo = []

    def mostrar_cartas_disponibles(self):
        self.lista_cartas.delete(0, tk.END)
        for carta in self.cartas_disponibles:
            self.lista_cartas.insert(tk.END, f"{carta['nombre']} - {carta['tipo_carta']}")

    def agregar_al_mazo(self):
        seleccion = self.lista_cartas.curselection()
        if not seleccion:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona una carta para agregar.")
            return
        
        carta_seleccionada = self.cartas_disponibles[seleccion[0]]
        tipo_carta = carta_seleccionada["tipo_carta"]

        # Validación de tamaño del mazo
        if len(self.mazo) >= self.deck_size:
            messagebox.showwarning("Mazo completo", f"El mazo solo puede contener {self.deck_size} cartas.")
            return

        # Validación de restricciones de tipo de carta
        contador_tipos = Counter(carta["tipo_carta"] for carta in self.mazo)
        max_tipo = int(self.deck_size * restricciones_tipo.get(tipo_carta, 0))

        if tipo_carta != "Básica" and contador_tipos[tipo_carta] >= max_tipo:
            messagebox.showwarning("Límite alcanzado", f"El mazo no puede tener más de {max_tipo} cartas de tipo {tipo_carta}.")
            return

        # Agregar carta al mazo y eliminarla de la lista de cartas disponibles
        self.mazo.append(carta_seleccionada)
        self.lista_mazo.insert(tk.END, f"{carta_seleccionada['nombre']} - {tipo_carta}")
        self.cartas_disponibles.pop(seleccion[0])
        self.mostrar_cartas_disponibles()

    def remover_del_mazo(self):
        seleccion = self.lista_mazo.curselection()
        if not seleccion:
            messagebox.showwarning("Selección inválida", "Por favor, selecciona una carta para remover.")
            return

        carta_removida = self.mazo.pop(seleccion[0])
        self.lista_cartas.insert(tk.END, f"{carta_removida['nombre']} - {carta_removida['tipo_carta']}")
        self.cartas_disponibles.append(carta_removida)
        self.lista_mazo.delete(seleccion[0])

    def guardar_mazo(self):
        nombre_mazo = self.entry_nombre.get().strip()
        
        if not nombre_mazo:
            messagebox.showwarning("Nombre requerido", "Por favor, ingresa un nombre para el mazo.")
            return

        if len(self.mazo) != self.deck_size:
            messagebox.showwarning("Mazo incompleto", f"El mazo debe contener exactamente {self.deck_size} cartas antes de guardarlo.")
            return

        # Preparar los datos del mazo para guardar
        nuevo_mazo = {
            "nombre": nombre_mazo,
            "cartas": self.mazo
        }

        # Agregar el mazo a la lista de mazos en el archivo JSON
        if "mazos" not in self.data:
            self.data["mazos"] = []
        
        self.data["mazos"].append(nuevo_mazo)

        # Guardar los datos actualizados en el archivo JSON del usuario
        with open(f"{self.username}.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

        messagebox.showinfo("Mazo guardado", f"El mazo '{nombre_mazo}' ha sido guardado exitosamente.")
        self.entry_nombre.delete(0, tk.END)
        self.lista_mazo.delete(0, tk.END)
        self.mazo.clear()
        self.mostrar_cartas_disponibles()

# Inicializar la aplicación con un usuario específico
if __name__ == "__main__":
    root = tk.Tk()
    app = DeckBuilderApp(root, "123_cuenta")  # Sustituir "nombre_usuario" con el usuario actual
    root.mainloop()
