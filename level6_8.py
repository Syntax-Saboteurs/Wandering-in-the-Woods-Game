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
ROWS = 10
COLS = 10
# this is where we get our size of each cell 
CELL_SIZE = (WIDTH // COLS, HEIGHT // ROWS)

# creates the window in which the game will display. The dimensions are (x, y)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sky_surface = pygame.image.load("graphics/sky.png").convert()

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
#snail_x_pos = 800
snail_rect = snail_surf.get_rect(midtop = (555,570))

player_surf = pygame.image.load('graphics/fly1.png').convert_alpha()
player_rect = player_surf.get_rect(midtop = (5, 4))

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

# get_input() function -- will get users input for grid 
def get_input(x):
    
    # empty 
    input_text = ''
    
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                # Check if the pressed key represents a digit (0-9)
                if event.unicode.isdigit():

                    # Append the digit to the input_text
                    input_text += event.unicode  

                elif event.key == pygame.K_RETURN:
                    
                    # Convert the input_text to an integer and return it when Enter is pressed
                    try:
                        return int(input_text)
                    except ValueError:
                        # Handle the case where the input_text cannot be converted to an integer
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Remove the last character if Backspace is pressed
                    input_text = input_text[:-1]  

        # Clear the screen
        screen.fill(FOREST_GREEN)

        if x == 2:
            text_surf_row = font.render("Select a number for the amount of rows: " + input_text, True, BLACK)
            screen.blit(text_surf_row, (10, 10))
        elif x == 3:
            text_surf_cols = font.render("Select a number for the amount of rows: " + input_text, True, BLACK)
            screen.blit(text_surf_cols, (10, 10))
        else:
            # Display the input text
            text_surface = font.render("Select 1 to start or select 2 to create grid: " + input_text, True, BLACK)
            screen.blit(text_surface, (10, 10))
        
        # Update the display
        pygame.display.update()

# create_text()function - takes five parameters -- what is to be said, in what font, display mode, location on screen
def create_text(text, font, screen, x, y):
    dialoge = font.render(text, 2, BLACK)
    textBox = dialoge.get_rect()
    textBox.topleft = (x, y)
    screen.blit(dialoge, textBox)

# draw_grid() function -- allows the user to create grid map and size
def draw_grid(l, r, c):
    
    # This sets up the amount of rows and columns in our grid - if we change these values the number of squares changes
    rows = r
    cols = c

    # this is where we get our size of each cell 
    cell_size = (WIDTH // cols, HEIGHT // rows)

    # if l (level) == 1 use the standard grid 
    if l == 1:
        
        # this creates the cells that correlate to the WIDTH
        for x in range(0, WIDTH, CELL_SIZE[0]):
            pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
        # this creates the cells that correlate to the HEIGHT
        for y in range(0, HEIGHT, CELL_SIZE[1]):
            pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))
            
    # else use the customizable draw_grid
    else:
        
        # this creates the cells that correlate to the WIDTH
        for x in range(0, WIDTH, cell_size[0]):
            pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
        # this creates the cells that correlate to the HEIGHT
        for y in range(0, HEIGHT, cell_size[1]):
            pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))
            
def main():
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    player_turn = 0  # 0 for player 1, 1 for player 2
    players = [player_rect, snail_rect]  # Assuming there are only two players
    win_font = pygame.font.SysFont(None, 48)  # Font for "You Win" message

    # Call the get_integer_input function to start receiving input
    lvl = get_input(0)
    rows = get_input(2)
    cols = get_input(3)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // (HEIGHT // ROWS)
                clicked_col = mouse_pos[0] // (WIDTH // COLS)
                current_player_rect = players[player_turn]
                current_row = current_player_rect.y // (HEIGHT // ROWS)
                current_col = current_player_rect.x // (WIDTH // COLS)

                # Check if the clicked position is adjacent to the current player position
                if (abs(clicked_row - current_row) <= 1 and abs(clicked_col - current_col) <= 1 and
                        (abs(clicked_row - current_row) != 0 or abs(clicked_col - current_col) != 0)):
                    current_player_rect.x = clicked_col * (WIDTH // COLS)
                    current_player_rect.y = clicked_row * (HEIGHT // ROWS)
                    # Switch to the next player's turn
                    player_turn = (player_turn + 1) % len(players)

        screen.blit(sky_surface, (0, 0))
        screen.blit(sky_surface, (0, 300))
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)
        
        draw_grid(lvl, rows, cols)

        # Check if players overlap
        if player_rect.colliderect(snail_rect):

            # Display "You Win" message
            win_text = win_font.render("You Win!", True, (255, 255, 255))
            win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(win_text, win_rect)

            #create_text('Total moves it took to collide: ', font, screen,  30, 10)
            cheer.play(fade_ms = 3000)
            
            # Stop the game loop
            #running = False

        pygame.display.update()
        clock.tick(600)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
