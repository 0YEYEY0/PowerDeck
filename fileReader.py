import json 
import os.path
 
# Reads through the entire json file
def read():
    # Opening JSON file
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)

        return json_object
    
    
#Alphabetically sorts the cards/file elements by name
def sorting(card):

    ordered = sorted(card, key=lambda d: d["nombre"])
    return ordered

# Function to create list with all values from one attribute of the album of cards
def cardAttribute(attribute, list):
    # Opening JSON file
    """
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
    """
    #Alphabetically sorts the cards
    sortedCards = sorting(list)

    #Find all values or text from specific card attribute 
    info = [card[attribute] for card in sortedCards]
    return info

# Function to find a specific´s card info based on its name
def cardInfo(id):
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)

    
    #Alphabetically sorts the cards/file elements
    sortedCards = sorting(json_object)

    #Find info from a specific card
    info = list(filter(lambda card: card["nombre"] == id, sortedCards))
    data = list (dict(info[0]).values()) # list of values 
    return data

def getMain():
    json_object = read()

    #Alphabetically sorts the cards/file elements
    sortedCards = sorting(json_object)

    #Find info from a specific card
    info = list(filter(lambda card: card["es_principal"] == True, sortedCards))
    #data = list (dict(info[0]).values()) # list of values 
    return info


# Function to check if file exist
def exists():
    check = os.path.isfile("./cartas.json")
    return check
