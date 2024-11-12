import pygame
import pygame.event
import pygame.transform
from fileReader import *
from Buttons import *
import json

def main(cuenta="admin"):
    
    pygame.init()

    # Configuración de la pantalla
    resolution = (720, 720)
    screen_color = (155, 255, 155)
    
    # Nombre de la ventana de pygame
    pygame.display.set_caption('PowerDeck')
    
    # Superficie de la pantalla
    screen = pygame.display.set_mode(resolution)
    
    # Configuración del juego
    timer = pygame.time.Clock()
    fps = 60
    
    # Pintar la pantalla una vez
    pygame.display.flip()
    status = True
    
    # Información básica para imágenes y texto de cartas
    imageSize = (140,140)
    imageLocation = (int(imageSize[0])//2), (int(imageSize[1])//2)
    font = pygame.font.SysFont(None, 40)
    
    # Función para dibujar la interfaz de usuario del álbum
    def draw_ui():
        pygame.draw.rect(screen, (102, 205, 170, 255), [0,120, 720, 700], 0, 10)
        text = font.render("ALBUM DE CARTAS", True, 'white')
        screen.blit(text, (250, 65))

    # Determina el archivo de cartas basado en el tipo de cuenta
    if cuenta == "admin":
        card_file = 'cartas.json'
    else: 
        card_file = cuenta

    with open(card_file, 'r', encoding="utf-8") as file:
        if card_file == 'cartas.json':
            card_data = json.load(file)
        else:
            player_data = json.load(file)
            card_data = player_data['cartas']
    
    # Obtener la ruta de la imagen desde los datos de la carta
    def get_image_path(name):
        for card in card_data:
            if card['nombre'] == name:
                return card['imagen']
        return None
    
    # Función para ordenar y obtener la imagen de una carta
    def imageAlbum(name):
        if not card_data:
            text = font.render("Álbum vacío", True, 'white')
            screen.blit(text, (250, 300))
            return pygame.Surface(imageSize)
    
        image_path = get_image_path(name)
        if image_path:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, imageSize)
            return image
        else:
            text = font.render(f"Imagen para {name} no encontrada.", True, 'white')
            screen.blit(text, (250, 300))
            return pygame.Surface(imageSize)
       
    # Lista para almacenar las ubicaciones de las cartas en pantalla
    cards = []
    
    # Crear ubicaciones de cartas en la pantalla
    def createCards(cardAmount):
        x, y = 80, 220
        cards.clear()  # Limpia la lista de ubicaciones de cartas
        for i in range(cardAmount):
            if x + int(imageSize[0]) > 900:
                x = 80
                y += imageSize[1]
            if y + int(imageSize[1]) > 720:  
                break
                
            cards.append(pygame.Rect(x, y, int(imageSize[0]), int(imageSize[1])))
            x += imageSize[0]
        return cards

    Album = []  # Álbum de cartas que se muestra
    # Bucle principal del juego
    while status:
        timer.tick(fps)
        screen.fill(screen_color)
        draw_ui()
    
        # Verifica si el archivo de cartas existe
        if not exists(card_file):
            text = font.render("¡NO HAY CARTAS CREADAS AÚN!", True, 'white')
            screen.blit(text, (180, 300))
        else:
            # Cuenta el total de cartas y crea las ubicaciones
            cardsTotal = len([element for element in card_data if isinstance(element, dict)])
            cardLocation = createCards(cardsTotal)
    
            # Botón de filtro
            filterImage = pygame.image.load("Imagenes/something.png")
            filterButton = Button(600,65,25,25,screen, False, filterImage,"Variants")
            if filterButton.pressed():
                cardsTotal = len([element for element in list(getMain(card_file)) if isinstance(element, dict)])
                cardLocation = createCards(cardsTotal)
                Album = getMain(card_file)
            else:
                Album = card_data
                
            # Muestra cartas y su información
            for i in range(cardsTotal):
                cardX = cardLocation[i].x
                cardY = cardLocation[i].y
                
                # Crea los botones de cartas
                Cardbutton = Button(cardX,cardY,imageSize[0],imageSize[1],screen, True, imageAlbum(cardAttribute("nombre", Album)[i]), str(cardAttribute("nombre", Album)[i]))
    
                # Muestra la información de la carta seleccionada
                if Cardbutton.pressed():
                    pygame.draw.rect(screen, "white", [15, 15, 690, 690], 0, 10)
                    pygame.draw.rect(screen, "black", [20, 20, 680, 680], 0, 10)
                    atributos = ["nombre", "variante", "raza", "tipo_carta", "activo_en_juego", "activo_en_paquetes", "id", "fecha_modificacion"]
                    y_offset = 65
                    for atributo in atributos:
                        text = font.render(f"{atributo.capitalize()}: {cardAttribute(atributo, Album)[i]}", True, 'white')
                        screen.blit(text, (100, y_offset))
                        y_offset += 40

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
    
        pygame.display.update()
        
    pygame.quit()
