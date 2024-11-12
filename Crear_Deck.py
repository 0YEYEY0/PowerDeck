import json
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class DeckManagerApp:
    def __init__(self, user_file):
        self.user_file = user_file
        self.load_user_data()
        self.deck_size = 5  # Tamaño máximo del mazo
        self.max_decks = 15  # Número máximo de mazos por usuario

        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Deck Manager")
        self.create_widgets()
        self.root.mainloop()

    def load_user_data(self):
        # Cargar la data del usuario desde el archivo JSON, si existe
        if os.path.exists(self.user_file):
            with open(self.user_file, "r") as f:
                try:
                    self.user_data = json.load(f)
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "El archivo JSON está vacío o tiene un formato incorrecto.")
                    self.user_data = {}
        else:
            messagebox.showerror("Error", "El archivo de usuario no existe.")
            self.user_data = {}

        # Cargar las cartas y los mazos
        self.cards = self.user_data.get("cartas", [])
        self.decks = self.user_data.get("mazos", [])

    def save_user_data(self):
        # Guardar la data actualizada del usuario en el archivo JSON
        self.user_data["mazos"] = self.decks
        with open(self.user_file, "w") as f:
            json.dump(self.user_data, f, indent=4)

    def create_widgets(self):
        # Crear la interfaz gráfica de usuario
        self.deck_name_entry = tk.Entry(self.root)
        self.deck_name_entry.grid(row=0, column=1)
        tk.Label(self.root, text="Nombre del mazo:").grid(row=0, column=0)
        
        self.create_deck_button = tk.Button(self.root, text="Crear Mazo", command=self.create_deck)
        self.create_deck_button.grid(row=0, column=2)

        self.show_decks_button = tk.Button(self.root, text="Mostrar Mazos", command=self.show_decks)
        self.show_decks_button.grid(row=1, column=0, columnspan=3)
        
        self.card_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.card_listbox.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.update_card_listbox()

        self.add_card_button = tk.Button(self.root, text="Agregar Carta al Mazo", command=self.add_card_to_deck)
        self.add_card_button.grid(row=3, column=0, columnspan=2)

        self.delete_deck_button = tk.Button(self.root, text="Eliminar Mazo", command=self.delete_deck)
        self.delete_deck_button.grid(row=4, column=0, columnspan=2)

    def update_card_listbox(self):
        # Actualizar la lista de cartas
        self.card_listbox.delete(0, tk.END)
        for card in self.cards:
            self.card_listbox.insert(tk.END, f"{card['nombre']} ({card['tipo_carta']})")

    def create_deck(self):
        # Crear un nuevo mazo
        if len(self.decks) >= self.max_decks:
            messagebox.showerror("Error", f"No se pueden crear más de {self.max_decks} mazos.")
            return
        
        deck_name = self.deck_name_entry.get().strip()
        if not deck_name:
            messagebox.showerror("Error", "Por favor, ingresa un nombre para el mazo.")
            return

        if any(deck["nombre"] == deck_name for deck in self.decks):
            messagebox.showerror("Error", "Ya existe un mazo con este nombre.")
            return

        # Agregar el nuevo mazo a la lista de mazos
        new_deck = {"nombre": deck_name, "cartas": []}
        self.decks.append(new_deck)
        self.save_user_data()
        messagebox.showinfo("Éxito", f"Mazo '{deck_name}' creado exitosamente.")

    def add_card_to_deck(self):
        # Agregar una carta seleccionada al mazo activo
        selected_card_index = self.card_listbox.curselection()
        if not selected_card_index:
            messagebox.showerror("Error", "Selecciona una carta para agregar al mazo.")
            return
        
        card = self.cards[selected_card_index[0]]
        deck_name = self.deck_name_entry.get().strip()
        
        deck = next((deck for deck in self.decks if deck["nombre"] == deck_name), None)
        if not deck:
            messagebox.showerror("Error", "Por favor, selecciona o crea un mazo primero.")
            return

        # Verificar si la carta ya está en el mazo
        if any(c['nombre'] == card['nombre'] and c['variante'] == card['variante'] for c in deck['cartas']):
            messagebox.showwarning("Advertencia", "Esta carta ya está en el mazo.")
            return

        # Verificar restricciones de cantidad por tipo
        tipo_carta = card["tipo_carta"]
        restricciones_tipo = {"Ultra Rara": 0.1, "Muy-Rara": 0.15, "Rara": 0.2, "Normal": 0.6, "Basica": 1.0}
        max_tipo = int(self.deck_size * restricciones_tipo.get(tipo_carta, 0))
        
        current_count = sum(1 for c in deck["cartas"] if c["tipo_carta"] == tipo_carta)
        if current_count >= max_tipo:
            messagebox.showerror("Error", f"El mazo no puede tener más de {max_tipo} cartas de tipo {tipo_carta}.")
            return

        if len(deck["cartas"]) >= self.deck_size:
            messagebox.showerror("Error", "El mazo ha alcanzado el tamaño máximo permitido.")
            return

        # Agregar la carta al mazo
        deck["cartas"].append(card)
        self.save_user_data()
        messagebox.showinfo("Éxito", f"Carta '{card['nombre']}' agregada al mazo '{deck_name}'.")

    def show_decks(self):
        # Mostrar todos los mazos creados por el usuario
        if not self.decks:
            messagebox.showinfo("Mazos", "No tienes mazos creados.")
            return
        
        deck_names = "\n".join(deck["nombre"] for deck in self.decks)
        selected_deck_name = simpledialog.askstring("Mazos", f"Tus mazos:\n\n{deck_names}\n\nIngresa el nombre de un mazo para ver sus cartas:")

        deck = next((deck for deck in self.decks if deck["nombre"] == selected_deck_name), None)
        if not deck:
            messagebox.showerror("Error", "No se encontró el mazo.")
            return

        card_names = "\n".join(card["nombre"] for card in deck["cartas"])
        messagebox.showinfo("Cartas en el mazo", f"Cartas en '{selected_deck_name}':\n\n{card_names}")

    def delete_deck(self):
        # Eliminar un mazo
        deck_name = simpledialog.askstring("Eliminar Mazo", "Ingresa el nombre del mazo que deseas eliminar:")
        deck = next((deck for deck in self.decks if deck["nombre"] == deck_name), None)
        if not deck:
            messagebox.showerror("Error", "No se encontró el mazo.")
            return

        self.decks.remove(deck)
        self.save_user_data()
        messagebox.showinfo("Éxito", f"Mazo '{deck_name}' eliminado exitosamente.")


# Ejecución del programa
if __name__ == "__main__":
    # Archivo de ejemplo para pruebas
    user_file = "123_cuenta.json"  # Cambia esto al nombre de archivo real según sea necesario
    DeckManagerApp(user_file)
