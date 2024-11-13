import pygame
import pygame.event
import pygame.transform
from fileReader import *
from Buttons import *
import json


def main(cuenta="admin"):
    
    pygame.init()


    # screen info
    resolution = (720, 720)
    screen_color = (155, 255, 155)
    
    # set the pygame window name
    pygame.display.set_caption('PowerDeck')
    
    # create the display surface object
    screen = pygame.display.set_mode(resolution)
    
    # Game setup 
    timer = pygame.time.Clock()
    fps = 60
    
    # Paints screen once
    pygame.display.flip()
    status = True
    
    # Basic info for cards image and text  
    imageSize = (140,140)
    imageLocation = (int(imageSize[0])//2), (int(imageSize[1])//2)
    font = pygame.font.SysFont(None, 40)
    
    
    # Basic UI for cards album
    def draw_ui():
        pygame.draw.rect(screen,(102, 205, 170, 255), [0,120, 720, 700], 0, 10)
        text = font.render("CARDS ALBUM", True, 'white')
        screen.blit(text, (250, 65))
        pass

    if cuenta == "admin":
        card_file = 'cartas.json'
    else: 
        card_file = cuenta
    
    with open(card_file, 'r') as file:
        if card_file == 'cartas.json':
            card_data = json.load(file)
        else:
            player_data = json.load(file)
            card_data = player_data['cartas']
    
    # Función para obtener la ruta de la imagen desde los datos de la carta
    def get_image_path(name):
        for card in card_data:
            if card['nombre'] == name:
                return card['imagen']
        return None
    
    # Función para ordenar todas las imágenes
    def imageAlbum(name):
        if not card_data:
            text = font.render("Álbum vacío", True, 'white')
            screen.blit(text, (250, 300))
            return pygame.Surface(imageSize)  # Devuelve una superficie en blanco si el álbum está vacío
    
        image_path = get_image_path(name)
        if image_path:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, imageSize)
            return image
        else:
            text = font.render(f"Imagen para {name} no encontrada.", True, 'white')
            screen.blit(text, (250, 300))
            return pygame.Surface(imageSize)  # Devuelve una superficie en blanco si la imagen no se encuentra
       
    # list to save cards location on the screen
    cards = []
    x, y = 80, 220
    
        
    # Creates cards location on the screen
    def createCards(cardAmount):
        x, y = 80, 220
        for i in range(cardAmount):
            if x + int(imageSize[0]) > 900:
                x = 80
                y += imageSize[1]
            if y + int(imageSize[1]) > 720:  
                break
                
            cards.append(pygame.Rect(x, y, int(imageSize[0]), int(imageSize[1])))
            x += imageSize[0]
        return cards
    Album = [] 
    # Card Album game loop
    while (status):
        timer.tick(fps)
        screen.fill(screen_color)
        draw_ui()
    
        #Verifies if any cards exists 
        if exists('cartas.json') == False:
            text = font.render("NO CARDS CREATED YET!", True, 'white')
            screen.blit(text, (180, 300))
        else:
            # Count number of cards created
            cardsTotal = res = len([element for element in list(read()) if isinstance(element, dict)])
            cardLocation = createCards(cardsTotal)
    
            # Filter button
            filterImage = pygame.image.load("Imagenes/something.png")
            filterButton = Button(600,65,25,25,screen, False, filterImage,"Variants")
            if filterButton.pressed():
                cardsTotal = res = len([element for element in list(getMain()) if isinstance(element, dict)])
                cardLocation = createCards(cardsTotal)
                Album = getMain()
                print(str(cardAttribute("nombre", Album)))
            else:
                Album = read()
                
            # View cards and info
            for i in range(cardsTotal):
                cardX = cardLocation[i].x
                cardY = cardLocation[i].y
                
                # Creates cards
                Cardbutton = Button(cardX,cardY,imageSize[0],imageSize[1],screen, True, imageAlbum(cardAttribute("nombre", Album)[i]), str(cardAttribute("nombre", Album)[i]))
    
                # Show cards-info function
                if Cardbutton.pressed():
                    pygame.draw.rect(screen, "white", [15, 15, 690, 690], 0, 10)
                    pygame.draw.rect(screen, "black", [20, 20, 680, 680], 0, 10)
                    # Name
                    text = font.render("Name: " + str(cardAttribute("nombre", Album)[i]), True, 'white')
                    screen.blit(text, (100, 65))
                    # Variant
                    text = font.render("Variant: " + str(cardAttribute("variante", Album)[i]), True, 'white')
                    screen.blit(text, (100, 100))
                    # Race
                    text = font.render("Race: " + str(cardAttribute("raza", Album)[i]), True, 'white')
                    screen.blit(text, (100, 140))
                    # Card Type
                    text = font.render("Card type: " + str(cardAttribute("tipo_carta", Album)[i]), True, 'white')
                    screen.blit(text, (100, 180))
                    # Status: Active/Inactive
                    text = font.render("Game Status: " + str(cardAttribute("activo_en_juego", Album)[i]), True, 'white')
                    screen.blit(text, (100, 220))
                    # Pack Status: Active/Inactive
                    text = font.render("Pack Status: " + str(cardAttribute("activo_en_paquetes", Album)[i]), True, 'white')
                    screen.blit(text, (100, 260))
                    # Id
                    text = font.render("Id: " + str(cardAttribute("id", Album)[i]), True, 'white')
                    screen.blit(text, (100, 300))
                    # Date of creation/modification
                    text = font.render("Date: " + str(cardAttribute("fecha_modificacion", Album)[i]), True, 'white')
                    screen.blit(text, (100, 340))
    
    
        for i in pygame.event.get():
     
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False
    
        pygame.display.update()
        
    # deactivates the pygame library
    pygame.quit()