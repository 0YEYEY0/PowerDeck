import pygame
import pygame.draw
import pygame.rect
 

# Inialize pygame font
pygame.font.init()


 # Button class
class Button():
    # Button methods
    def __init__(self, x, y, width, height,  screen, active, img, text):

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
        self.active = active
        self.img = img
        self.rect = self.img.get_rect(center=(self.x, self.y))
        self.draw()
        self.click = False
        self.action = False


    # Draw buttons method
    def draw(self):
        ''' Method for updating button effects '''
        # Button text  and font  
        font = pygame.font.SysFont('freesansbold.ttf', 18)
        button_text = font.render(self.text, True, self.fgcolor)
        button_text2 = font.render(self.text, True, "black")
        text_rect = button_text.get_rect(center=(self.x, self.y))
        text_rect2 = button_text2.get_rect(center=(self.x, self.y))
        button_rect = pygame.rect.Rect((self.x, self.y), (self.width, self.height))
        button_rectHighlight = pygame.rect.Rect((self.x-2, self.y-2), (self.width+4, self.height+4))


        if self.active == True:
            if self.hover():
                pygame.draw.rect(self.screen, (69, 139, 116, 255), self.rect, 0, 0)
                self.screen.blit(button_text, text_rect)
            else:
                self.screen.blit(self.img, self.rect)
        else:
            self.rect = button_rectHighlight
            pygame.draw.rect(self.screen, "black", button_rectHighlight, 0, 10)
            pygame.draw.rect(self.screen, (139, 131, 120, 255), button_rect, 0, 10)
            self.screen.blit(button_text2, text_rect2)

        

        
    # Check if button´s clicked method
    def pressed (self):
        pointer = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.rect)
         
        # Button conditions (Mouse clicked)
        if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(pointer):

            return True
        else:
            return False   
    
    # Check if button´s clicked method
    def clicked (self):
        pointer = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.rect)
         
        # Button conditions (Mouse clicked)
        if button_rect.collidepoint(pointer):
            if pygame.mouse.get_pressed()[0] == 1:
                self.click = True
                #return True
                #print ("Hola")
                self.action = True
            elif pygame.mouse.get_pressed()[0] == 0 and self.click == True:
                self.click=False  
                #return True
                self.action = True
        return self.action
     
    # Check if mouse is near the button method 
    def hover(self):
        pointer = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect(self.rect)
         
        #Button conditions (Mouse near button)

        if button_rect.collidepoint(pointer):
            return True
        else:
            return False
