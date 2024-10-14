import pygame
import pygame.draw
 

# Inialize pygame font
pygame.font.init()

 
class Button():
    #Button methods
    def __init__(self, x, y, width, height,  screen, img, text):

        # Set Button Attributes
        self.border_color = 'black'
        self.bgcolor = 'darkgray'
        self.fgcolor = 'white'
        self.bg_hover_color = 'dimgrey'
        self.fg_hover_color = 'white'
        self.text = text
        self.width = width
        self.height = height 
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.rect = self.img.get_rect(center=(self.x, self.y))
        self.draw()


    
    def draw(self):
        ''' Method for updating button effects '''
        # Button text  and font  
        font = pygame.font.SysFont('freesansbold.ttf', 18)
        button_text = font.render(self.text, True, self.fgcolor)
        text_rect = button_text.get_rect(center=(self.x, self.y))
 
        if self.hover():
            pygame.draw.rect(self.screen, "dark gray", self.rect, 0, 0)
            self.screen.blit(button_text, text_rect)
        else:
            self.screen.blit(self.img, self.rect)

        
         
    def pressed (self):
        pointer = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.rect)
         
        # Button conditions (Mouse clicked)
        if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(pointer):

            return True
        else:
            return False    
    
    def hover(self):
        pointer = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.rect)
         
        #Button conditions (Mouse near button)

        if button_rect.collidepoint(pointer):
            return True
        else:
            return False
    