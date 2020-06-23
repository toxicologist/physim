"""

Basic physics simulation in Python

-pygame for visual rendering
-vectors for forces
-etc..

"""

import pygame

from pygame.locals import *

w, h = 800, 600
speed = [-10, -10]

pygame.init()
pygame.display.set_caption('physics sim')
running = True

display = pygame.display.set_mode((w, h), RESIZABLE)
surf = pygame.Surface((w, h))
clock = pygame.time.Clock()

cpos = [5, 5]

while running:
    display.fill((255, 255, 255))
    clock.tick(60)

    cpos[0] -= speed[0]
    cpos[1] -= speed[1]

    c = pygame.draw.circle(display, (255, 0, 0), cpos, 20)

    # collision check
    if cpos[0] < 0 or cpos[0] > w:
        speed[0] = -speed[0]

    elif cpos[1] < 0 or cpos[1] > h:
        speed[1] = -speed[1]

    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()

pygame.quit()
