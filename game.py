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
    first = True

    # CONTROLS
    left_press, right_press, up_press, down_press = False, False, False, False

    # WINDOW SETUP
    size_x, size_y = 700, 500
    size = (size_x, size_y)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Frog vs Cilantro")
    pygame.mouse.set_visible(False)
    myfont = pygame.font.SysFont("monospace", 16)

    # OBJECT INSTANTIATION
    title_image = pygame.image.load("img/title.jpg")

    background_image = pygame.image.load("img/background.jpg")

    player = player("Rick", 300 , 200 , "img/frontfrog1.png", "img/frontfrog2.png",
                    "img/backfrog1.png", "img/backfrog2.png", size_x, size_y)

    c_ul = cilantro("c_ul", 10, 10, "img/cilantro1.png", "img/cilantro2.png",
                  "img/cilantro3.png", 1, player.getPos(), size_x, size_y)

    c_ml = cilantro("c_ur", size_x / 2 - 50, 10, "img/cilantro1.png", "img/cilantro2.png",
                  "img/cilantro3.png", 1, player.getPos(), size_x, size_y)

    c_mr = cilantro("c_ll", size_x / 2 + 50, 10, "img/cilantro1.png", "img/cilantro2.png",
                  "img/cilantro3.png", 1, player.getPos(), size_x, size_y)
    c_ur = cilantro("c_lr", size_x - 10, 10, "img/cilantro1.png", "img/cilantro2.png",
                  "img/cilantro3.png", 1, player.getPos(), size_x, size_y)
    c_list = [c_ul, c_ml, c_mr, c_ur]

    # CLOCK
    running, title, clock = True, True, pygame.time.Clock()

    # TITLE SCREEN
    while(title):
        # DRAW TITLE
        screen.blit(title_image, [0, 0])

        # User did something
        for event in pygame.event.get():
            # User exited window
            if event.type == pygame.QUIT:
                running = False
            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    title = False

        # UPDATE
        pygame.display.flip()

        # LIMIT TO 60 FPS
        clock.tick(60)

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

        # DRAW BACKGROUND
        screen.blit(background_image, [0, 0])

        # DRAW SCORE
        scoretext = myfont.render("Score {0}".format(score // 60), 1, (0,0,0))
        screen.blit(scoretext, (5, 10))

        # GAME LOGIC
        player.move(left_press, right_press, up_press, down_press)
        screen.blit(player.getImage(), player.getPos())
        for c in c_list:
            c.move()
            screen.blit(c.getImage(), c.getPos())
            # COLLISION
            if (not first and player.collide(c)):
                running = False
                break
            c.refresh(player.getPos())

        # Undo first run
        first = False

        # UPDATE
        pygame.display.flip()

        # LIMIT TO 60 FPS
        clock.tick(60)

    # QUIT THE GAME
    pygame.quit()

    # Scores
    print("Your Score: " + str(score // 60))
