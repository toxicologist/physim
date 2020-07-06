# cool demo

import pygame

import random

from pygame.locals import *

import math

from math import radians

w, h = 1000, 1000

GREEN = (0, 255, 60)

pygame.init()
pygame.display.set_caption('cool demo')
running = True

display = pygame.display.set_mode((w, h), RESIZABLE)
surf = pygame.Surface((w, h))
clock = pygame.time.Clock()

center = [int(x / 2) for x in (w, h)]
line_length = int(w / 2.5)

# cool animation thingy
n = 1
inc = 1.01


def fround(n):  # fix shitty float precision
    small_float = 0.000001
    if 0 < n < small_float or 0 > n > -small_float:
        return 0
    else:
        return n


def cos(n):
    return fround(math.cos(n))


def sin(n):
    return fround(math.sin(n))


def draw_line(start, end, w=1):
    return pygame.draw.aaline(display, GREEN, start, end, w)


def cool_animation_thingy():
    global n
    global inc
    upper = 1.5
    lower = 1
    n *= inc

    if n > upper or n < lower:
        inc = 1 / inc
        n = n ** inc
        # n = lower

    # print(n)

    for i in range(100):
        mult = n ** i
        draw_line((center[0] + line_length / mult, center[1] + line_length / mult),
                  (center[0] - line_length / mult, center[1] + line_length / mult))


def get_extremities(degree_increment, line_length=line_length):
    line_extremities = []

    for i in range(math.ceil(360 / degree_increment)):
        deg = degree_increment * i

        deg = radians(deg)
        line_extremities.append(
            (math.ceil(center[0] + line_length * cos(deg)), math.ceil(center[1] - line_length * sin(deg))))

    return line_extremities


def draw_line_dots(deg_inc, times=5, offset=0):
    phi = (1 + math.sqrt(5)) / 2
    l = line_length

    for i in range(times):
        l = math.ceil(l / phi)
        for e in get_extremities(deg_inc, line_length=l + offset):
            pygame.draw.circle(display, GREEN, e, 2)


# cool animation 2
d = 1
d_inc = 0.1


def cool_animation_2():
    global d
    global d_inc

    lower = 1
    upper = 35

    d += d_inc
    if d > 7 or d < 0.3:
        d_inc = -d_inc
        d += d_inc

    for e in get_extremities(d):
        draw_line(e, center)

    draw_line_dots(d, offset=d * random.randint(98, 100) / 10)


while running:
    clock.tick(35)
    display.fill((0, 0, 0))

    cool_animation_thingy()
    cool_animation_2()

    pygame.draw.circle(display, GREEN, center, 10, 1)

    pygame.draw.circle(display, GREEN, center, line_length, 2)

    # radius lines

    #ex = get_extremities(45)
    #for e in ex:
    #    draw_line(center, e)
    #    draw_line_dots(45, 10)

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
