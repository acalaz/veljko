import sys
import pygame
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
running = True

class Actor:
    def __init__(self):
        Actor.__init__(self, 0, 0, 32, 32)
        self.directions = [False, False, False, False]
        self.speed = 0.1

    def rotate(self, angle):
        rot_image = pygame.transform.rotozoom(self.surface, angle, 1)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.rotated_surface = rot_image

    def move(self):
        if self.directions[0]:
            self.y -= self.speed
        if self.directions[1]:
            self.y += self.speed
        if self.directions[2]:
            self.x -= self.speed
        if self.directions[3]:
            self.x += self.speed

    def draw(self):
        screen.blit(self.rotated_surface, (self.x, self.y))

player = Player()

def redraw():
    screen.fill((75, 0, 0))
    player.draw()
    player.move()
    pygame.display.flip()

while (running):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
            if e.key == pygame.K_w:
                player.directions[0] = True
            if e.key == pygame.K_s:
                player.directions[1] = True
            if e.key == pygame.K_a:
                player.directions[2] = True
            if e.key == pygame.K_d:
                player.directions[3] = True
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                player.directions[0] = False
            if e.key == pygame.K_s:
                player.directions[1] = False
            if e.key == pygame.K_a:
                player.directions[2] = False
            if e.key == pygame.K_d:
                player.directions[3] = False
        elif e.type == pygame.MOUSEMOTION:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            angle = math.atan2(mouse_y - player.y, mouse_x - player.x)
            angle = angle * (180 / math.pi)
            player.rotate(angle)

    redraw()