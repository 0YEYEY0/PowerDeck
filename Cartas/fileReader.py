import json
import os.path

# Lee todo el contenido del archivo JSON
def read(filename='Cartas/cartas.json'):
    # Abre el archivo JSON
    with open(filename, 'r') as openfile:
        # Lee el contenido del archivo JSON
        json_object = json.load(openfile)

        # Verifica si el archivo es 'cartas.json' o si existe el atributo 'cartas'
        if filename == 'Cartas/cartas.json':
            return json_object
        else:
            return json_object.get("cartas", [])

# Ordena alfabéticamente las cartas por nombre
def sorting(cards):
    ordered = sorted(cards, key=lambda d: d["nombre"].lower())
    return ordered

# Crea una lista con todos los valores de un atributo específico de las cartas
def cardAttribute(attribute, cards):
    # Ordena alfabéticamente las cartas
    sortedCards = sorting(cards)

    # Encuentra todos los valores del atributo específico de las cartas
    info = [card[attribute] for card in sortedCards]
    return info

def llaves_cartas(attribute, cards):
    # Ordena alfabéticamente las cartas

    # Encuentra todos los valores del atributo específico de las cartas
    info = [card[attribute] for card in cards]
    return info

# Crea una lista con todos los atributo  de las cartas
def atributos():

    info = list(set().union(*(cartas["atributos"].keys() for cartas in read())))
    return info

# Crea una lista con todos los valores de un atributo específico de las cartas
def atributos_valores(atributo, cards):
    # Ordena alfabéticamente las cartas
    sortedCards = sorting(cards)

    # Encuentra todos los valores del atributo específico de las cartas
    info = [card["atributos"][atributo] for card in sortedCards]
    return info

# Busca la información de una carta específica basada en su nombre
def cardInfo(name, filename='Cartas/cartas.json'):
    cards = read(filename)
    sortedCards = sorting(cards)

    # Encuentra la información de una carta específica
    info = list(filter(lambda card: card["nombre"] == name, sortedCards))
    if info:
        data = list(dict(info[0]).values())  # Lista de valores
        return data
    else:
        return None

# Obtiene las cartas marcadas como principales
def getMain(filename='Cartas/cartas.json'):
    cards = read(filename)
    sortedCards = sorting(cards)

    # Encuentra las cartas marcadas como 'principal'
    info = list(filter(lambda card: card.get("es_principal", False), sortedCards))
    return info

# Verifica si el archivo existe
def exists(filename='Cartas/cartas.json'):
    return os.path.isfile(filename)

#print(cardInfo("Sprint2"))
#print(atributos_valores("Amabilidad", read()))