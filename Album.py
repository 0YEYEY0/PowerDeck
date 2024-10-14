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
#a = res = len([element for element in list(read()) if isinstance(element, dict)])
#print(a)

#print ("All names: " +  str(cardAttribute("nombre")))
#print ("Molly card:" + str(cardInfo("Molly")))



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

    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False


    
    pygame.display.update()
    
# deactivates the pygame library
pygame.quit()
