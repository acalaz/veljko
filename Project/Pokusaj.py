import pygame as pg
from math import atan2, degrees
wn = pg.display.set_mode((1300, 700))
pg.init()
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Strelica.png")
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()



    def point_at(self, x, y):
        rotated_image = pg.transform.rotate(self.image, degrees(atan2(x-self.rect.x, y-self.rect.y)))
        new_rect = rotated_image.get_rect(center=self.rect.center)
        wn.fill((255, 255, 255))
        wn.blit(rotated_image, new_rect.topleft)




player = Player()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEMOTION:
            player.point_at(*pg.mouse.get_pos())

    pg.display.update()