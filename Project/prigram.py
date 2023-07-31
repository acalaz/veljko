import pygame as pg
pg.init
WIDTH = 800
HEIGHT = 600
lopticay = 0
lopticax = 0
screen = pg.display.set_mode((WIDTH, HEIGHT))
while True:
    screen.fill((0, 0, 0))
    if lopticay == 0 and lopticax >= 0 and lopticax != 800:
        lopticax += 2
    elif lopticax == 800 and lopticay >= 0 and lopticay != 600:
        lopticay += 2
    elif lopticax <= 800 and lopticay == 600 and lopticax != 0:
        lopticax -= 2
    else:
        lopticay -= 2
    pg.draw.circle(screen, (255, 255, 255), (lopticax, lopticay), 30)
    pg.display.update()
    pg.time.delay(1)
    print(lopticax, lopticay)
    