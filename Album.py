import pygame
import pygame.transform
from fileReader import *
from Buttons import *

# activate the pygame library .
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

# Count number of cards created
a = res = len([element for element in list(read()) if isinstance(element, dict)])
print(a)

print ("All names: " +  str(cardAttribute("nombre")))
print ("Molly card:" + str(cardInfo("Molly")))



# Paints screen once
pygame.display.flip()
status = True
imageSize = (140,140)
imageLocation = (int(imageSize[0])//2)+10, (int(imageSize[1])//2)+150

font = pygame.font.SysFont(None, 40)


#Basic UI for cards album
def draw_ui():
    pygame.draw.rect(screen,(102, 205, 170, 255), [0,120, 720, 700], 0, 10)
    text = font.render("CARDS ALBUM", True, 'white')
    screen.blit(text, (250, 65))
    pass
# sorts through all images
def imageAlbum(name):
    image = pygame.image.load("./" + str(name) + ".PNG")
    image = pygame.transform.scale(image, imageSize)
    return image

# Card Album game loop
while (status):
    timer.tick(fps)
    screen.fill(screen_color)
    draw_ui()

    if a == 0:
        text = font.render("NO CARDS CREATED YET!", True, 'white')
        screen.blit(text, (250, 300))
    else:
        for cardsNumX in range (a):
            for cardsNumY in range (a):
                if cardsNumX < int(resolution[0])//int(imageSize[0]):
                    x = (cardsNumX*int(imageSize[0]))+int(imageLocation[0])
                    y = int(imageLocation[1])
                    if cardsNumY < int(resolution[1])//int(imageSize[1]):
                        x = int(imageLocation[0]) 
                        y= (cardsNumY*int(imageSize[1]))+(int(imageLocation[1]))  
                    else:
                        cardsNumY = 0
                else:
                    cardsNumX = 0

                Cardbutton = Button(x,y,imageSize[0],imageSize[1],screen,imageAlbum(cardAttribute("nombre")[cardsNumX]), str(cardAttribute("nombre")[cardsNumX]))

                if Cardbutton.pressed():
                    pygame.draw.rect(screen, "white", [15, 15, 690, 690], 0, 10)
                    pygame.draw.rect(screen, "black", [20, 20, 680, 680], 0, 10)
                    # Name
                    text = font.render("Name: " + str(cardAttribute("nombre")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 65))
                    # Variant
                    text = font.render("Variant: " + str(cardAttribute("variante")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 100))
                    # Race
                    text = font.render("Race: " + str(cardAttribute("raza")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 140))
                    # Card Type
                    text = font.render("Card type: " + str(cardAttribute("tipo_carta")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 180))
                    # Status: Active/Inactive
                    text = font.render("Game Status: " + str(cardAttribute("activo_en_juego")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 220))
                    # Pack Status: Active/Inactive
                    text = font.render("Pack Status: " + str(cardAttribute("activo_en_paquetes")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 260))
                    # Id
                    text = font.render("Id: " + str(cardAttribute("id")[cardsNumX]), True, 'white')
                    screen.blit(text, (100, 300))
                    # Date of creation/modification
                    text = font.render("Date: " + str(cardAttribute("fecha_modificacion")[cardsNumX]), True, 'white')
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
