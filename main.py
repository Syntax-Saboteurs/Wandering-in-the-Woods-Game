import levelk_2
import level3_5
import level6_8
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption('Wondering in the woods game!')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

splash_surface = pygame.image.load('graphics/Woodplank.jpeg')

text_surface = test_font.render('Welcome chose a level',False,"Black")
font = pygame.font.SysFont('Arial', 40)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
            
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def levelK():
    levelk_2.main()
    print('K-2 Button Pressed')

def level3():
    level3_5.main()
    print('3-5 Button Pressed')

def level6():
    level6_8.main()
    print('6-8 Button Pressed')


Button(170, 150, 100, 50, 'K-2', levelK)
Button(170, 200, 100, 50, '3-5', level3)
Button(170, 250, 100, 50, '6-8', level6)
# Button(170, 200, 100, 50,  '3-5', level3, True) multi click buttons
# Button(170, 250, 100, 50,  '6-8', level6, True) multi click buttons

#grade_level = input("Enter the grade level (K-2, 3-5, or 6-8): ").strip().lower()

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
