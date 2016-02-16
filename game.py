from math import *
from objects import *
from colors import *
from stickman import *
from player import *
from entity import *

import pygame

class game:

    # INITIALIZE GAME
    pygame.init()
    colors = colors()

    # CONTROLS
    left_press, right_press, up_press, down_press = False, False, False, False 

    # WINDOW SETUP
    size_x, size_y = 700, 500
    size = (size_x, size_y)
    BG_COLOR = colors.BLUE()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)

    # OBJECT INSTANTIATION
    background_image = pygame.image.load("background.jpg")
    player = player("Frog", size_x // 2, size_y // 2, pygame.image.load("player.png"))

    # WINDOW RUN TIME
    running, clock, obj = True, pygame.time.Clock(), objects()
    while (running):
        # MAIN EVENT LOOP
        for event in pygame.event.get(): # User did someting
            if event.type == pygame.QUIT:
                running = False
            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    left_press = True
                elif event.key == pygame.K_d:
                    right_press = True 
                elif event.key == pygame.K_w:
                    up_press = True 
                elif event.key == pygame.K_s:
                    down_press = True
            # User let up on a key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    left_press = False
                elif event.key == pygame.K_d:
                    right_press = False 
                elif event.key == pygame.K_w:
                    up_press = False 
                elif event.key == pygame.K_s:
                    down_press = False

        # GAME LOGIC
        player.move(left_press, right_press, up_press, down_press)

        # DRAWING CODE
        #screen.fill(BG_COLOR) # clear screen
        screen.blit(background_image, [0, 0])
        screen.blit(player.img, player.getPos())

        # UPDATE
        pygame.display.flip()

        # LIMIT TO 60 FPS
        clock.tick(60)

    # QUIT THE GAME
    pygame.quit()
