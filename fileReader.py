import json
import os.path

# Reads through the entire json file
def read(file_path='cartas.json'):
    # Opening JSON file
    with open(file_path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        
        # If the file is not 'cartas.json', extract the 'cartas' attribute
        if file_path != 'cartas.json':
            json_object = json_object.get('cartas', [])
        
        return json_object

# Reads through all json file
def lector(path):
    # Opening JSON file
    with open(path, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        
        return json_object
# Alphabetically sorts the cards/file elements by name
def sorting(card):
    ordered = sorted(card, key=lambda d: d["nombre"])
    return ordered

# Function to create list with all values from one attribute of the album of cards
def cardAttribute(attribute, list):
    # Alphabetically sorts the cards
    sortedCards = sorting(list)

    # Find all values or text from specific card attribute 
    info = [card[attribute] for card in sortedCards]
    return info

# Function to find a specific card's info based on its name
def cardInfo(id, file_path='cartas.json'):
    json_object = read(file_path)
    
    # Alphabetically sorts the cards/file elements
    sortedCards = sorting(json_object)

    # Find info from a specific card
    info = list(filter(lambda card: card["nombre"] == id, sortedCards))
    data = list(dict(info[0]).values()) if info else [] # list of values 
    return data

def getMain(file_path='cartas.json'):
    json_object = read(file_path)

    # Alphabetically sorts the cards/file elements
    sortedCards = sorting(json_object)

    # Find info from a specific card
    info = list(filter(lambda card: card["es_principal"] == True, sortedCards))
    return info

# Function to check if file exists
def exists(file_path='cartas.json'):
    check = os.path.isfile(file_path)
    return check
