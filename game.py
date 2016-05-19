import math
import random

from colors import *
from player import *
from entity import *
from cilantro import *

import pygame

class game:

    # INITIALIZE GAME
    pygame.init()
    score = 0

    # CONTROLS
    left_press, right_press, up_press, down_press = False, False, False, False 

    # WINDOW SETUP
    size_x, size_y = 700, 500
    size = (size_x, size_y)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Frog vs Cilantro")
    pygame.mouse.set_visible(False)

    # OBJECT INSTANTIATION
    background_image = pygame.image.load("img/background.jpg")
    player = player("Rick", 300 , 200 , 
                    "img/frontfrog1.png", "img/frontfrog2.png", 
                    "img/backfrog1.png", "img/backfrog2.png", 
                    size_x, size_y)
    c_slow = cilantro("c", 0, 0, 
                  "img/cilantro1.png", "img/cilantro2.png",
                  "img/cilantro3.png", 1, player.getPos())

    # WINDOW RUN TIME
    running, clock, lose = True, pygame.time.Clock(), False

    # MAIN EVENT LOOP
    while (running):
        # Update Player Score
        score += 1

        # User did someting
        for event in pygame.event.get(): 
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
        c_slow.move()

        # DRAWING CODE
        #screen.fill(BG_COLOR) # clear screen
        screen.blit(background_image, [0, 0])
        screen.blit(player.getImage(), player.getPos())
        screen.blit(c_slow.getImage(), c_slow.getPos())

        # Test Collision
        if (player.collide(c_slow)):
            running = False

        # UPDATE
        pygame.display.flip()

        # LIMIT TO 60 FPS
        clock.tick(60)

    # QUIT THE GAME
    pygame.quit()

    # Scores
    print("Your Score: " + str(score))
