import pygame as pg
pg.init
WIDTH = 1356
HEIGHT = 700
green = (0, 150, 0)
red = (200, 0, 0)
black = (0, 0, 0)
pg.display.set_caption("Asteroids")
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
GH = 250
rect3 = ((0,HEIGHT//1.5 ), (WIDTH, GH))
pg.draw.rect(screen, green, rect3)
pg.display.update()
pg.time.delay(2000)
sombrero = [(),(),(),(),(),(),(),()]
#whil e tr ue:
#    for event in pygame.event.get(): 
# 
#      if event.type == pygame.QUIT:
#         pygame.quit()
