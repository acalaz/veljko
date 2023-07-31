import sys, pygame, math;
from pygame.locals import *;
pygame.init()
screen = pygame.display.set_mode((800, 600))
mousec = pygame.image.load("cursor-png-1127(1).png").convert_alpha()
pygame.transform.scale(mousec, (10,10))
space_ship = pygame.image.load("Strelica.png").convert_alpha()
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("test1")
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print("test3")
    screen.fill('white')
    pos = pygame.mouse.get_pos()
    #screen.blit(mousec, (pos))
    angle = 360-math.atan2(pos[1]-300,pos[0]-400)*180/math.pi
    rotimage = pygame.transform.rotate(space_ship,angle)
    rect = rotimage.get_rect(center=(400,300))
    screen.blit(rotimage,rect) #I need space_ship to rotate towards my cursor
    pygame.display.update()
