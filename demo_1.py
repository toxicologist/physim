"""

Basic physics simulation in Python

-pygame for visual rendering
-vectors for forces
-etc..

"""

import pygame

from pygame.locals import *

from lib.vector import Vector

import math

from math import radians

w, h = 1000, 1000
speed_vector = Vector(45, 1)

GREEN = (0, 255, 60)

pygame.init()
pygame.display.set_caption('cool demo')
running = True

display = pygame.display.set_mode((w, h), RESIZABLE)
surf = pygame.Surface((w, h))
clock = pygame.time.Clock()

center = [int(x/2) for x in (w,h)]
line_length = int(w / 2.5)


# cool animation thingy
n = 1
inc = 1.01


def fround(n): # fix shitty float precision
    small_float = 0.000001
    if n > 0 and n < small_float or n < 0 and n > -small_float:
        return 0
    else:
        return n


def cos(n):
    return fround(math.cos(n))


def sin(n):
    return fround(math.sin(n))


def draw_line(start, end, w=1):
    return pygame.draw.line(display, GREEN, start, end, w)


def cool_animation_thingy():
    global n
    global inc
    n *= inc

    if n > 1.5 or n < 1:
       inc = 1/inc
       n *= inc

    #print(n)

    for i in range(25):
        mult = n ** i
        draw_line((center[0] + line_length / mult, center[1] + line_length / mult), (center[0] - line_length / mult, center[1] + line_length / mult))


def get_extremities(degree_increment):
    line_extremities = []

    for i in range(math.ceil(360 / degree_increment)):

        deg = radians(degree_increment * i)
        line_extremities.append(((center[0] + line_length * cos(deg)), math.ceil(center[1] + line_length * sin(deg))))

    return line_extremities


# cool animation 2
d = 1
d_inc = 0.8


def cool_animation_2():
    global d
    global d_inc

    d += d_inc
    if d > 35 or d < 1:
        d_inc = -d_inc
        d += d_inc

    for e in get_extremities(d):
        draw_line(e, center)


while running:
    clock.tick(25)
    display.fill((0,0,0))

    cool_animation_thingy()
    cool_animation_2()

    pygame.draw.circle(display, GREEN, center, 10, 1)

    pygame.draw.circle(display, GREEN, center, line_length, 2)

    # radius lines

    #ex = get_extremities(45)
    #for e in ex:
    #    draw_line(e, center)

    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), RESIZABLE)
            w, h = event.w, event.h

        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()

pygame.quit()
