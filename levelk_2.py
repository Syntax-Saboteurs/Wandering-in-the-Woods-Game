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
CELL = (ROWS, COLS)

# this is where we get our size of each cell 
CELL_SIZE = (WIDTH // COLS, HEIGHT // ROWS)

# creates the window in which the game will display. The dimensions are (x, y)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sky_surface = pygame.image.load("graphics/sky.png").convert()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(topleft = ((5,4)))

player_surf = pygame.image.load('graphics/player/player_walk_1.png')
player_rect = player_surf.get_rect(center = (555,570))

# create new size 
snail_surf = pygame.transform.scale(snail_surf, (CELL_SIZE))
player_surf = pygame.transform.scale(player_surf, (CELL_SIZE))

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


# sounds -- https://www.sounds-resource.com/
# background sound - works just add sound file
cheer = pygame.mixer.Sound('sounds/cheer.wav')
collision = pygame.mixer.Sound('sounds/collision.wav')
pygame.mixer.music.load('sounds/space.mp3')
pygame.mixer.music.play(-1, 0.0)


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

# main() function 
def main():

    # running set to True
    running = True

    # creates diplay screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # 0 for player 1, 1 for player 2
    player_turn = 0
    # for total moves to reach eachother
    # total = 0
    # Assuming there are only two players
    players = [player_rect, snail_rect]
    
    # Font for "You Win" message
    win_font = pygame.font.SysFont(None, 48)  

    # while True
    while running:

        # loop through events
        for event in pygame.event.get():
            # if event is equivalent to QUIT
            if event.type == pygame.QUIT:
                # set running to False
                running = False
            # if mouse clicked down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mouse_pos is the location of mouse position
                mouse_pos = pygame.mouse.get_pos()
                # clicked_row
                clicked_row = mouse_pos[1] // (HEIGHT // ROWS)
                # clicked_col
                clicked_col = mouse_pos[0] // (WIDTH // COLS)

                  
                current_player_rect = players[player_turn]

                # current_row 
                current_row = current_player_rect.y // (HEIGHT // ROWS)
                # current_col
                current_col = current_player_rect.x // (WIDTH // COLS)

                # Check if the clicked position is adjacent to the current player position
                if (abs(clicked_row - current_row) <= 1 and
                    abs(clicked_col - current_col) <= 1 and
                   (abs(clicked_row - current_row) != 0 or
                    abs(clicked_col - current_col) != 0)):
                    current_player_rect.x = clicked_col * (WIDTH // COLS)
                    current_player_rect.y = clicked_row * (HEIGHT // ROWS)

                    # Switch to the next player's turn
                    player_turn = (player_turn + 1) % len(players)
                    # total = player_turn + 1
            
        # creates the background and objects in the game level
        screen.blit(sky_surface, (0, 0))
        screen.blit(sky_surface, (0, 300))
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)

        # call draw grid() function
        draw_grid()

        # Check if players overlap
        if player_rect.colliderect(snail_rect):
            # Display "You Win" message -- changed color to black
            win_text = win_font.render("You Win!", True, (0, 0, 0))
            win_rect = win_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(win_text, win_rect)

            #create_text('Total moves it took to collide: ', font, screen,  30, 10)
            cheer.play(fade_ms = 3000)
            # possibly add a key option to screen to see if they would like to play again
        
            # ask user if they would like to play again??
            
            pygame.display.flip()
            # Stop the game loop
            # running = False
                    
        pygame.display.update()
        
        #pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
