import json
import os
from datetime import datetime
import random
import string

# Ruta del archivo JSON donde se almacenan las cartas
FILE_PATH = 'cartas.json'

# Valores predefinidos para las razas oficiales y tipos de carta
RAZAS_OFICIALES = ['Humano', 'Elfo', 'Orco', 'Dragón', 'ángel', 'Demonio']
TIPOS_CARTA = ['Ultra-Rara', 'Muy-Rara', 'Rara', 'Normal', 'Basica']


# Función para validar los atributos de la carta
def validar_atributos(atributos):
    """Valida que los valores de los atributos sean numéricos y estén entre -100 y 100."""
    for valor in atributos.values():
        if not isinstance(valor, int) or not (-100 <= valor <= 100):
            return False, f"Los atributos deben estar entre -100 y 100. Valor inválido: {valor}"
    return True, ""


# Función para validar Turno de Poder y Bonus de Poder
def validar_turno_bonus(turno_poder, bonus_poder):
    """Valida que Turno de Poder y Bonus de Poder estén entre 0 y 100."""
    if not (0 <= turno_poder <= 100):
        return False, "El Turno de Poder debe estar entre 0 y 100."
    if not (0 <= bonus_poder <= 100):
        return False, "El Bonus de Poder debe estar entre 0 y 100."
    return True, ""


# Función para verificar si ya existe una carta con el mismo nombre y variante
def carta_duplicada(nombre, variante, cartas):
    """Verifica si ya existe una carta con el mismo nombre y variante."""
    for carta in cartas:
        if carta['nombre'] == nombre and carta['variante'] == variante:
            return True
    return False


# Función para generar un identificador único para cada carta
def generar_id_unico():
    """Genera un identificador único para la carta y su variante."""
    return "C-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + \
        "-V-" + ''.join(random.choices(string.ascii_letters + string.digits, k=12))


# Función para verificar si ya existe una carta con el mismo nombre de personaje
def es_variante(nombre, cartas):
    """Determina si la carta es una variante al verificar si ya existe una carta con el mismo nombre."""
    for carta in cartas:
        if carta['nombre'] == nombre:
            return True
    return False


# Función para validar que los campos requeridos no estén vacíos y cumplan con las restricciones de longitud
def validar_campos_obligatorios(nombre, descripcion, variante, raza, tipo_carta):
    """Valida que los campos obligatorios no estén vacíos, cumplan con las longitudes mínimas/máximas y tengan valores válidos."""
    if not (5 <= len(nombre.strip()) <= 30):
        return False, "El nombre debe tener entre 5 y 30 caracteres."
    if not (5 <= len(variante.strip()) <= 30):
        return False, "El nombre de la variante debe tener entre 5 y 30 caracteres."
    if len(descripcion.strip()) > 1000:
        return False, "La descripción no puede tener más de 1000 caracteres."
    if raza not in RAZAS_OFICIALES:
        return False, f"La raza debe ser una de las siguientes: {', '.join(RAZAS_OFICIALES)}."
    if tipo_carta not in TIPOS_CARTA:
        return False, f"El tipo de carta debe ser uno de los siguientes: {', '.join(TIPOS_CARTA)}."
    return True, ""


# Función para guardar una carta en el archivo JSON
def guardar_carta(nombre, descripcion, variante, raza, tipo_carta, turno_poder, bonus_poder, atributos, imagen_path):
    """Guarda una nueva carta en el archivo JSON si pasa las validaciones necesarias."""

    # Validar que los campos requeridos no estén vacíos y cumplan las restricciones
    campos_validos, mensaje_error = validar_campos_obligatorios(nombre, descripcion, variante, raza, tipo_carta)
    if not campos_validos:
        raise ValueError(mensaje_error)

    # Validar atributos
    atributos_validos, mensaje_error = validar_atributos(atributos)
    if not atributos_validos:
        raise ValueError(mensaje_error)

    # Validar Turno de Poder y Bonus de Poder
    turno_bonus_validos, mensaje_error = validar_turno_bonus(turno_poder, bonus_poder)
    if not turno_bonus_validos:
        raise ValueError(mensaje_error)

    # Cargar cartas existentes
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            cartas = json.load(file)
    else:
        cartas = []

    # Determinar si es variante o principal
    es_principal = not es_variante(nombre, cartas)
    variante = "Principal" if es_principal else "variante"

    # Verificar si la combinación nombre + variante ya existe
    if carta_duplicada(nombre, variante, cartas):
        raise ValueError(f"Ya existe una carta con el nombre '{nombre}' y la variante '{variante}'.")

    # Generar la nueva carta
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    carta = {
        'id': generar_id_unico(),
        'nombre': nombre,
        'descripcion': descripcion,
        'variante': variante,
        'es_principal': es_principal,
        'raza': raza,
        'tipo_carta': tipo_carta,
        'turno_poder': turno_poder,
        'bonus_poder': bonus_poder,
        'atributos': atributos,
        'poder_total': sum(atributos.values()),
        'imagen': imagen_path,
        'fecha_creacion': fecha_actual,
        'fecha_modificacion': fecha_actual,
        'activo_en_juego': True,
        'activo_en_paquetes': True
    }

    # Guardar la nueva carta
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
