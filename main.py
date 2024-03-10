import pygame, levelk_2, level3_5, level6_8
from pygame.locals import *
#from sys import exit

# initializes pygame
pygame.init()
screen = pygame.display.set_mode((450,450))

# captions -- the user already knows it is a game no need in adding it to the display
pygame.display.set_caption('WONDERING IN THE WOODS')
clock = pygame.time.Clock()

# fonts
test_font = pygame.font.Font(None,50)
font = pygame.font.SysFont('Arial', 40)

splash_surface = pygame.image.load('graphics/backgrounds/woods.png')
text_surface = test_font.render('CHOOSE A LEVEL', False, "Black")

# fonts
#test_font = pygame.font.Font(None,50)
font = pygame.font.SysFont('Arial', 40)

objects = []

# class Button -- used to create button objects
class Button:
    # __init__() method -- takes eight parameters
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        # has this button been pressed yet -- set to False
        self.alreadyPressed = False
        
        # creates the color scheme for the mouse effects
        self.fillColors = {         # normal was #ffffff
                            'normal': '#3ECA1F',
                            'hover': '#666666',
                            'pressed': '#333333',
                          }
        
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        
        # adding button object to the objects[] list
        objects.append(self)
        
    # process() method -- checks if mouse has pressed obj or is hovering obj
    def process(self):
        # mousePos is the position where the pointer is
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        # if button selected (clicked)
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            # if buttons pressed fill
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                
                if self.onePress:
                    self.onclickFunction()
                
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
                
        # create buttons surfaces
        self.buttonSurface.blit(self.buttonSurf,[
                                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                                ])
        
        # create the buttons to screen
        screen.blit(self.buttonSurface, self.buttonRect)

def levelK():
    levelk_2.main()
    print('LEVEL: I')

def level3():
    level3_5.main()
    print('LEVEL: II')

def level6():
    level6_8.main()
    print('LEVEL: III')
    player.main()
    
# buttons are created at these locations, dimensions, text, calls
Button(170, 150, 100, 50, 'LVL: I', levelK)
Button(170, 200, 100, 50, 'LVL: II', level3)
Button(170, 250, 100, 50, 'LVL: III', level6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(splash_surface,(0,0))
    screen.blit(text_surface,(40,110))
    for object in objects:
        object.process()
        
    pygame.display.update()
    clock.tick(30)
    
