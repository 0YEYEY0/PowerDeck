import json
import os
from datetime import datetime
import secrets
import random
import string

# Ruta del archivo JSON donde se almacenan las cartas
FILE_PATH = 'cartas.json'

# Función para validar los atributos de la carta
def validar_atributos(atributos):
    """Valida que todos los valores de los atributos sean enteros positivos."""
    for valor in atributos.values():
        if not isinstance(valor, int) or valor < 0:
            return False
    return True

# Función para generar un identificador único para cada carta
def generar_id_unico(nombre_carta, nombre_variante):
    return "C-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + \
           "-V-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# Función para guardar una carta en el archivo JSON
def guardar_carta(nombre, descripcion, variante, raza, tipo_carta, turno_poder, bonus_poder, atributos, imagen_path):
    """Guarda una nueva carta en el archivo JSON si pasa las validaciones necesarias."""
    if not validar_atributos(atributos):
        raise ValueError("Los atributos no son válidos. Deben ser enteros positivos.")

    # Carga las cartas existentes del archivo JSON si existe
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            cartas = json.load(file)
    else:
        cartas = []

    # Generar la carta nueva
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    carta = {
        'id': generar_id_unico(nombre, variante),
        'nombre': nombre,
        'descripcion': descripcion,
        'variante': variante,
        'es_principal': variante.lower() == 'principal',
        'raza': raza,
        'tipo_carta': tipo_carta,
        'turno_poder': turno_poder,
        'bonus_poder': bonus_poder,
        'atributos': atributos,
        'poder_total': sum(atributos.values()),
        'imagen': imagen_path,
        'fecha_creacion': fecha_actual,
        'fecha_modificacion': fecha_actual,
        'activo_en_juego': True,  # Puede ser modificado en el futuro según tu lógica
        'activo_en_paquetes': True  # Igual que el campo anterior
    }

    # Verifica si la carta ya existe por su ID
    if any(c['id'] == carta['id'] for c in cartas):
        raise ValueError(f"Ya existe una carta con el ID {carta['id']}.")

    # Agrega la carta a la lista de cartas y guarda el archivo
    cartas.append(carta)
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(cartas, file, ensure_ascii=False, indent=4)

    return True

# Función para cargar las cartas existentes desde el archivo JSON
def cargar_cartas():
    """Carga las cartas desde el archivo JSON."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Función para obtener una carta específica por su ID
def obtener_carta_por_id(carta_id):
    """Obtiene una carta por su ID."""
    cartas = cargar_cartas()
    for carta in cartas:
        if carta['id'] == carta_id:
            return carta
    return None

# Función para modificar una carta existente
def modificar_carta(carta_id, nuevos_datos):
    """Modifica una carta existente por su ID."""
    cartas = cargar_cartas()
    carta_modificada = None

    # Busca la carta por su ID
    for carta in cartas:
        if carta['id'] == carta_id:
            # Actualiza los datos de la carta
            carta.update(nuevos_datos)
            carta['fecha_modificacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            carta_modificada = carta
            break

    if carta_modificada is None:
        raise ValueError(f"No se encontró una carta con el ID {carta_id}.")

    # Guarda las cartas nuevamente en el archivo JSON
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(cartas, file, ensure_ascii=False, indent=4)

    return carta_modificada

# Función para eliminar una carta por su ID
def eliminar_carta(carta_id):
    """Elimina una carta existente por su ID."""
    cartas = cargar_cartas()
    cartas_actualizadas = [carta for carta in cartas if carta['id'] != carta_id]

    if len(cartas) == len(cartas_actualizadas):
        raise ValueError(f"No se encontró una carta con el ID {carta_id} para eliminar.")

    # Guarda las cartas actualizadas en el archivo JSON
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(cartas_actualizadas, file, ensure_ascii=False, indent=4)

    return True
