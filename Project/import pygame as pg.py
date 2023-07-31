import pygame as pg
import time
pg.init()
clock = pg.time.Clock()
screen_width = 600
screen_height = 480
wn = pg.display.set_mode((screen_width, screen_height))
x = 20
y = 460
const = 12
while True:
    wn.fill((255, 255, 255))
    pg.draw.rect(wn, "Red", ((x, y), (100, 50)))
    y-=const
    const -= 0.2
    if y > 1300:
        x = 100
    clock.tick(100)
    pg.display.update()