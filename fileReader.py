import json 
 
def read():
    # Opening JSON file
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        

        return json_object
    
    
#Alphabetically sorts the cards by name
def sorting(card):

    ordered = sorted(card, key=lambda d: d["nombre"])
    return ordered

def cardAttribute(attribute):
    # Opening JSON file
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
    
    sortedCards = sorting(json_object)
    #Find all values or text from specific card attribute 
    info = [d[attribute] for d in sortedCards]
    return info

def cardInfo(id):
    with open('cartas.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)

    sortedCards = sorting(json_object)
    #Alphabetically sorts the cards by name
    #ordered = sorted(json_object, key=lambda d: d["name"])

    #Find info from a specific card
    info = list(filter(lambda card: card["nombre"] == id, sortedCards))
    data = list (dict(info[0]).values()) # list of values 
    #data = dict(info[0]) # values with titles dictionary
    return data

