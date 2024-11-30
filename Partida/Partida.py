import pygame
import pygame.event
import pygame.transform
import sys 
import os
sys.path.append(os.path.abspath('C:/Users/menei/Documents/GitHub/PowerDeck/Cartas'))
sys.path.append(os.path.abspath('C:/Users/menei/Documents/GitHub/PowerDeck/Jugadores'))
#sys.path.append(os.path.abspath('C:/Users/josec/Downloads/Projects/PowerDeck/PowerDeck/Cartas'))

import fileReader as fileReader
import Buttons as Buttons
import json
import random

def partida(cuenta, cantidad_mano_cartas=5):
    
    pygame.init()

    # Configuración de la pantalla
    pantalla_x = 1000
    pantalla_y = 720
    resolucion = (pantalla_x, pantalla_y)
    pantalla_color = (155, 255, 155)

    # Configuración visual del jugador/rival
    contenedor_mano_jugador_coordenadas = ((pantalla_x/4), pantalla_y-(pantalla_y/5))
    contenedor_mano_jugador_dimensiones = (pantalla_x-(pantalla_x/4)*2, pantalla_y)
    contenedor_mano_rival_coordenadas = (pantalla_x/4, 0)
    contenedor_mano_rival_dimensiones = (pantalla_x-(pantalla_x/4)*2, pantalla_y-(pantalla_y/5)*4)

    contenedor_pila_cartas_jugador_coordenadas = (((pantalla_x/4)+(pantalla_x-(pantalla_x/4)*2))+75, pantalla_y-(pantalla_y/5))
    contenedor_pila_cartas_jugador_dimensiones = (75,100)
    contenedor_pila_descarte_jugador_coordenadas = ((pantalla_x/4)-150, pantalla_y-(pantalla_y/5))
    contenedor_pila_descarte_jugador_dimensiones = (75,100)

    contenedor_pila_cartas_rival_coordenadas = (((pantalla_x/4)+(pantalla_x-(pantalla_x/4)*2))+75, 50)
    contenedor_pila_cartas_rival_dimensiones = (75,100)
    contenedor_pila_descarte_rival_coordenadas = ((pantalla_x/4)-150, 50)
    contenedor_pila_descarte_rival_dimensiones = (75,100)

    contenedor_manos_color = (102, 205, 170, 255)

    # configuración visual de las cartas
    ancho_carta = round(((contenedor_mano_jugador_dimensiones[0])/cantidad_mano_cartas)-1)
    largo_carta = round(((contenedor_mano_jugador_dimensiones[1]-contenedor_mano_jugador_coordenadas[1]))-4)
    imageSize = (ancho_carta, largo_carta)
    font_cartas = pygame.font.SysFont(None, 30)
    font_cartas_atributos = pygame.font.SysFont(None, 15)

    # configuración visual del temporizador
    temporizador_coordenadas = ((contenedor_mano_jugador_coordenadas[0]+contenedor_mano_jugador_dimensiones[0]) + 70,
                                (pantalla_y/2)+30)
    font_temporizador = pygame.font.SysFont(None, 20)
    
    # información de temporizador 
    reloj = pygame.time.Clock()
    contador = 10
    tiempo = 10
    texto_temporizador = str(tiempo).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # configuración visual del atributo de la ronda
    atributo_ronda_coordenadas = ((contenedor_mano_jugador_coordenadas[0]+contenedor_mano_jugador_dimensiones[0])+30,
                                (pantalla_y/2))
    font_atributo_ronda = pygame.font.SysFont(None, 18)
    atributos_carta = random.choice(fileReader.atributos())
    decision_ronda = None
    victorias = 0
    derrotas = 0 
    empate = 0
    rondas = 0

    # Nombre de la ventana de pygame
    pygame.display.set_caption('PowerDeck Partida')
    
    # Superficie de la pantalla
    pantalla = pygame.display.set_mode(resolucion)
    
    # Configuración del juego
    timer = pygame.time.Clock()
    fps = 60
    
    # Pintar la pantalla una vez
    pygame.display.flip()
    status = True

    # Función para dibujar contenedor de la mano de los jugadores
    def mano_jugadores():
        # Manos del jugador-rivales
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_mano_jugador_coordenadas, contenedor_mano_jugador_dimensiones), 0, 10)
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_mano_rival_coordenadas, contenedor_mano_rival_dimensiones), 0,
                            border_bottom_left_radius=10, border_bottom_right_radius=10)
        # Pila de cartas
        pantalla.blit(font_cartas.render("Pila de cartas", True, (0, 0, 0)), 
                      (contenedor_pila_cartas_jugador_coordenadas[0]-25,contenedor_pila_cartas_jugador_coordenadas[1]-25))
        pantalla.blit(font_cartas.render("Pila de cartas rival", True, (0, 0, 0)), 
                      (contenedor_pila_cartas_rival_coordenadas[0]-45,contenedor_pila_cartas_rival_coordenadas[1]+100))
        
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_pila_cartas_jugador_coordenadas, contenedor_pila_cartas_jugador_dimensiones), 0, 10)
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_pila_cartas_rival_coordenadas, contenedor_pila_cartas_rival_dimensiones), 0,10)
        # Pila de descarte
        pantalla.blit(font_cartas.render("Pila de descarte", True, (0, 0, 0)), 
                      (contenedor_pila_descarte_jugador_coordenadas[0]-50,contenedor_pila_descarte_jugador_coordenadas[1]-25))
        pantalla.blit(font_cartas.render("Pila de descarte rival", True, (0, 0, 0)), 
                      (contenedor_pila_descarte_rival_coordenadas[0]-65,contenedor_pila_descarte_rival_coordenadas[1]+100))
        
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_pila_descarte_jugador_coordenadas, contenedor_pila_descarte_jugador_dimensiones), 0, 10)
        pygame.draw.rect(pantalla, contenedor_manos_color, 
                         (contenedor_pila_descarte_rival_coordenadas, contenedor_pila_descarte_rival_dimensiones), 0,10)
        
    def area_juego():
        rect = pygame.Rect(0, 0, 500, 400)
        rect.center = (500, 360)
        pygame.draw.rect(pantalla, "white", rect)
                
    card_file = cuenta

    # Cargar datos de las cartas del archivo JSON
    with open(card_file, 'r', encoding="utf-8") as file:
        player_data = json.load(file)
        #card_data = player_data['cartas']
        
        mazo = player_data.get('mazos', [])[0].get('cartas', [])  
        #print(mazo)
        mano = mazo[:cantidad_mano_cartas]
    
    # Cargar datos de las cartas del bot
    with open('Jugadores/mazo_bot.json', 'r', encoding="utf-8") as file:
        bot_data = json.load(file)
        #card_data = player_data['cartas']
        
        mazo_bot = bot_data.get('mazos', [])[0].get('cartas', [])  
        #print(mazo)
        mano_bot = mazo_bot[:cantidad_mano_cartas]

    # Obtener la ruta de la imagen desde los datos de la carta
    def get_image_path(name):   
        for carta in mano:
            if carta['nombre'] == name:
                return carta['imagen']
        return None
    
    # Función para ordenar y obtener la imagen de una carta
    def imageAlbum(name):
        #if not card_data:
        if not mano:
            text = font_cartas.render("Álbum vacío", True, 'white')
            pantalla.blit(text, (250, 300))
            return pygame.Surface(imageSize)
    
        image_path = get_image_path(name)
        if image_path:
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, imageSize)
            return image
        else:
            text = font_cartas.render(f"Imagen para {name} no encontrada.", True, 'white')
            pantalla.blit(text, (250, 300))
            return pygame.Surface(imageSize)
       
    # Lista para almacenar las ubicaciones de las cartas en pantalla
    cards = []
    
    # Crear ubicaciones de cartas en la pantalla
    def createCards(cardAmount):
        
        x, y = contenedor_mano_jugador_coordenadas[0], contenedor_mano_jugador_coordenadas[1]
        cards.clear()  # Limpia la lista de ubicaciones de cartas
        for i in range(cardAmount):
            if x + int(imageSize[0]) > contenedor_mano_jugador_dimensiones[0]+contenedor_mano_jugador_coordenadas[0]:
                x = contenedor_mano_jugador_coordenadas[0] + imageSize[0]
                y += imageSize[1]
            if y + int(imageSize[1]) > contenedor_mano_jugador_dimensiones[1]+contenedor_mano_jugador_coordenadas[1]:  
                break
                
            cards.append(pygame.Rect(x, y, int(imageSize[0]), int(imageSize[1])))
            x += imageSize[0]
        return cards
        
       
    # Mostrar la carta seleccionada y su atributo
    def display_selected_card(card):
        pantalla.blit(imageAlbum(card['nombre']), (250, 150))
        print(card['nombre'])
        attribute_value = card['atributos'].get(atributos_carta)
        text = font_cartas.render(f"{atributos_carta.capitalize()}: {attribute_value}", True, 'black')
        pantalla.blit(text, (250, 300))
        return attribute_value

    def display_selected_card_bot(card):
        pantalla.blit(imageAlbum(card['nombre']), (400, 150))
        #print(card['nombre'])
        attribute_value = card['atributos'].get(atributos_carta)
        text = font_cartas.render(f"{atributos_carta.capitalize()}: {attribute_value}", True, 'black')
        pantalla.blit(text, (400, 300))
        return attribute_value

    Album = []  # Álbum de cartas que se muestra

    # Bucle principal del juego
    while status:
        timer.tick(fps)
        pantalla.fill(pantalla_color)
        mano_jugadores()
        area_juego()
        selected_card = None
        card_selected = False
    
        # Cuenta el total de cartas y crea las ubicaciones
        cardLocation = createCards(cantidad_mano_cartas)

        #Album = card_data
        Album = mano
            
        # Muestra cartas y su información
        for i in range(len(cardLocation)):
            cardX = cardLocation[i].x
            cardY = cardLocation[i].y

            # Verifica si aún quedan cartas en el mazo para esta posición
            if i < len(Album):
                # Crea los botones de cartas
                Cardbutton = Buttons.Button(
                    cardX,
                    cardY,
                    imageSize[0],
                    imageSize[1],
                    pantalla,
                    True,
                    imageAlbum(Album[i]['nombre']),
                    str(Album[i]['nombre'])
                )

                # Muestra la información de la carta seleccionada
                if Cardbutton.hover() and not pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(pantalla, "white", [300, 300, 345, 140], 0, 10)
                    pygame.draw.rect(pantalla, "black", [305, 305, 335, 130], 0, 10)
                    atributos = ['Amabilidad', 'Velocidad', 'SabidurÃ\xada', 'Prudencia', 'Resistencia', 'Balance', 'Defensa',
                                'Liderazgo', 'Confianza', 'Fuerza', 'Inteligencia', 'Altura', 'Flexibilidad', 'Lealtad', 'Explosividad',
                                'CoordinaciÃ³n', 'ValentÃ\xada', 'Poder', 'Disciplina', 'PercepciÃ³n', 'Agilidad', 'Habilidad', 'Carisma',
                                'Salto', 'Magia', 'Suerte']
                    y_offset = 315
                    x_offset = 315
                    for atributo in atributos:
                        text = font_cartas_atributos.render(f"{atributo.capitalize()}: {fileReader.atributos_valores(atributo, Album)[i]}", True, 'white')
                        pantalla.blit(text, (x_offset, y_offset))
                        y_offset += 20
                        if y_offset > 435:
                            x_offset += 85
                            y_offset = 315

                if not card_selected:
                    if Cardbutton.hover() and pygame.mouse.get_pressed()[0]:
                        print(f"Carta seleccionada: {Album[i]['nombre']} (índice {i})")
                        selected_card = Album.pop(i)  # Remover la carta seleccionada del mazo
                        card_selected = True
                        attribute_value = display_selected_card(selected_card)
                        print(f"Atributo {atributos_carta} de la carta seleccionada: {attribute_value}")
                        atributos_carta = random.choice(fileReader.atributos())  # Cambiar atributo
                        contador = 10  # Reiniciar el contador de tiempo
                        # Reemplaza la carta eliminada con otra del mazo, si queda alguna
                        if i < len(Album):
                            if len(mazo) > 0:
                                new_card = mazo.pop()
                                Album.insert(i, new_card)  # Toma la última carta y la coloca en la posición actual
                                Cardbutton.image = imageAlbum(new_card['nombre'])
                            else:
                                print("Mazo vacío")

                if card_selected:
                    pantalla.blit(imageAlbum(selected_card['nombre']), (250, 150))
                    attribute_value = selected_card['atributos'].get(atributos_carta)
                    text = font_cartas.render(
                        f"{atributos_carta.capitalize()}: {attribute_value}", True, 'black')
                    pantalla.blit(text, (250, 300))
                    
                    if len(mazo_bot) > 0:
                        selected_card_bot = mano_bot.pop(random.randint(0, len(mano_bot) - 1))
                        attribute_value_bot = display_selected_card_bot(selected_card_bot)
                        new_bot_card = mazo_bot.pop()
                        mano_bot.insert(i, new_bot_card)
                    else:
                        print("Mano del bot vacía")

                    if attribute_value > attribute_value_bot:
                        decision_ronda = "gano"
                        rondas +=1
                    if attribute_value < attribute_value_bot:
                        decision_ronda = "perdio"
                        rondas += 1
                    if attribute_value == attribute_value_bot:
                        decision_ronda = "empate"
                    if decision_ronda == "gano":
                        victorias +=1
                    if decision_ronda == "perdio":
                        derrotas +=1

                if contador <= 0 and not card_selected:
                    selected_card = Album.pop(random.randint(0, len(Album) - 1))  # Carta seleccionada al azar
                    card_selected = True
                    attribute_value = display_selected_card(selected_card)
                    print(f"Tiempo agotado. Carta seleccionada al azar: {selected_card['nombre']}")
                    atributos_carta = random.choice(fileReader.atributos())  # Cambiar atributo
                    contador = 10  # Reiniciar el contador de tiempo
                    if i < len(Album):
                        new_card = mazo.pop()
                        Album.insert(i, new_card)  # Toma la última carta y la coloca en la posición actual
                        Cardbutton.image = imageAlbum(new_card['nombre'])
                
        pygame.draw.rect(pantalla, "white", [(temporizador_coordenadas[0] - 5, temporizador_coordenadas[1] - 5), (80, 20)], 0, 0)
        pygame.draw.rect(pantalla, "black", [(temporizador_coordenadas[0] - 5, temporizador_coordenadas[1] - 5), (80, 20)], 5, 0)
        pantalla.blit(font_temporizador.render("Tiempo:" + texto_temporizador, True, (0, 0, 0)), temporizador_coordenadas)

        # Muestra el atributo ronda
        pygame.draw.rect(pantalla, "blue", [(atributo_ronda_coordenadas[0] - 5, atributo_ronda_coordenadas[1] - 5), (145, 20)], 0, 0)
        pygame.draw.rect(pantalla, "black", [(atributo_ronda_coordenadas[0] - 5, atributo_ronda_coordenadas[1] - 5), (145, 20)], 5, 0)
        pantalla.blit(font_atributo_ronda.render("Atributo:" + str(atributos_carta), True, (0, 0, 0)), atributo_ronda_coordenadas)

        # Muestra el # rondas
        pygame.draw.rect(pantalla, "white", [(50, atributo_ronda_coordenadas[1]), (145, 20)], 0, 0)
        pygame.draw.rect(pantalla, "black", [(50, atributo_ronda_coordenadas[1]), (145, 20)], 5, 0)
        pantalla.blit(font_atributo_ronda.render("# de rondas:" + str(rondas//4), True, (0, 0, 0)), 
                      ((55, atributo_ronda_coordenadas[1] + 5), (50, atributo_ronda_coordenadas[1])))
        
        # Muestra victorias/derrotas de rondas
        pygame.draw.rect(pantalla, "white", [(50, atributo_ronda_coordenadas[1] + 50), (145, 40)], 0, 0)
        pygame.draw.rect(pantalla, "black", [(50, atributo_ronda_coordenadas[1] + 50), (145, 40)], 5, 0)
        pantalla.blit(font_atributo_ronda.render("Victorias:" + str(victorias//4), True, (0, 0, 0)), 
                      ((55, atributo_ronda_coordenadas[1] + 55), (50, atributo_ronda_coordenadas[1])))
        pantalla.blit(font_atributo_ronda.render("Derrotas:" + str(derrotas//4), True, (0, 0, 0)), 
                      ((55, atributo_ronda_coordenadas[1] + 75), (50, atributo_ronda_coordenadas[1])))

        for i in pygame.event.get():
            if i.type == pygame.USEREVENT: 
                contador -= 1
                texto_temporizador = str(contador).rjust(3) if contador > 0 else 'Cambio!'

            if i.type == pygame.QUIT:
                status = False
        
        
        pygame.display.update()
        reloj.tick(60)
        
    pygame.quit()

partida("Jugadores/12345_cuenta.json")
