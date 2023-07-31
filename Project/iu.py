import pygame as pg
import time
import math
pg.init()
r = 40
xpos = 20
ypos = 20
def racunjanjehip(a,b):
    return math.sqrt(math.pow(a, 2),math.pow(b, 2))
while True:
    for event in pg.event.get:
        if pg.event.type == pg.MOUSEBUTTONDOWN:
            clicked = True
        elif pg.event.type == pg.MOUSEBUTTONUP:
            if clicked:
                if racunjanjehip(xpos, ypos) < r:
                    xpos = pg.mouse.get_pos[0]
                    ypos = pg.mouse.get_pos[1]

