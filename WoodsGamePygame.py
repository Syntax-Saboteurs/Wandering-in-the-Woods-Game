'''
resources: https://www.pygame.org/docs/

'''

import pygame, time, sys, random
from pygame.locals import *
# Constants
# This is for the width and height of our screen 
WIDTH   = 600
HEIGHT  = 600 
# This sets up the amount of rows and columns in our grid - if we change these values the number of squares changes
ROWS = 5
COLS = 5
# this is where we get our size of each cell 
CELL_SIZE = (WIDTH // COLS, HEIGHT // ROWS)

# creates the window in which the game will display. The dimensions are (x, y)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sky_surface = pygame.image.load("graphics/sky.png").convert()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_x_pos = 800
snail_rect = snail_surf.get_rect(midtop = (538,524))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midtop = (60,20))



# color tuples Constants - made of (r, g, b) if all are 255 it is white and if all values are zero then it is black - dont know what we will be using yet
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FOREST_GREEN = (190, 255, 0)


# pygame setup - this initializes pygame
pygame.init()


# clock object which will track the game to FPS as seen below
clock = pygame.time.Clock()
    
# limits FPS to 60 - important for game graphics 
clock.tick(40)  

# displaying name of the game: Wandering Woods
pygame.display.set_caption("Wandering Woods")

# removes the coursor from the game. Dont know if we should keep or not (does work)
# pygame.mouse.set_visible(False)

# set up font (style, size)
font = pygame.font.SysFont(None, 30)

# create_text()function - takes five parameters -- what is to be said, in what font, display mode, location on screen
def create_text(text, font, screen, x, y):
    dialoge = font.render(text, 2, BLACK)
    textBox = dialoge.get_rect()
    textBox.topleft = (x, y)
    screen.blit(dialoge, textBox)

def draw_grid():
    # this creates the cells that correlate to the WIDTH
    for x in range(0, WIDTH, CELL_SIZE[0]):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    # this creates the cells that correlate to the HEIGHT
    for y in range(0, HEIGHT, CELL_SIZE[1]):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


# level_one() function - game level for grades(k-2) 
def level_one():
    # grids are always square there are always two players starting diagonally from one another
    # wander out randomly - assuming they control their direction
    # each move is counted in a counter
    # music plays as cartoon characters wander in the woods
    # when the players bump into each other
        # there is happy graphics displayed
        # and stats from the wandering are displayed and announced audibly
        # then the game is reset and the students can start it up again if they would like
    return

# level_two() function - game level grades(3-5)
def level_two():
    # students can set up the size of their grid, which can now also be rectangular
    # there can be more than two players as many as four
    # students can place them where ever they want to on the grid to start
    # Once a pair has found eachother the pair will then search out another and another assuming more than two players
    # Once the game is started
        # it can be played and replayed over and over
        # the stats of the players meeting can be displayed as:
            # longest run without meeting
            # shorted run without meeting
            # and average run without meeting
            # assuming this means for all games played          
    return

# level_three() function - game level for grades(6-8)
def level_three():
    # students have control of 3-5 game (level II)
    # students will now be challanged to run experiments to determine how the average run varies with
        # size and shape of the grids.
    # the students will also be able to explore differnt protocols for wandering, and to decide which is
        # the best way to wander if you want to shorten the time it takes to meet up
    return


def main():
    
    running = True
    
    while running:
        moved = 0
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # can make a terminate or kill function to replace the logic here
                running = False

   
        screen.blit(sky_surface,(0,0))
        screen.blit(sky_surface,(0,300))
        screen.blit(snail_surf,snail_rect)
        screen.blit(player_surf,player_rect)


#when player is clicked they move TODO code diffrent directions and to stay in side barriers
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if player_rect.collidepoint((mouse_pos)):
                print ("mouse alien")
                player_rect.x += 110
            elif snail_rect.collidepoint((mouse_pos)):
                print ("mouse snail")
                snail_rect.x -= 110
            else: 
                print("missed")



                
          

        # calls the draw_grid() fuction to create the background
        draw_grid()
        


        # updates the display
        pygame.display.update()
        clock.tick(60)
        

    # this must be in the code in order for pygame to work in idle
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
