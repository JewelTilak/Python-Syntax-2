import pygame
from random import randint
import sys
pygame.init()

screen = pygame.display.set_mode([500,500])

clock = pygame.time.Clock()

class Circle():
    def __init__(self, x = None, y = None, r = None, color = None):
        self.x = x if x is not None else randint(-50,500)
        self.y = y if y is not None else randint(0,500)
        self.r = r if r is not None else randint(10,50)
        self.color = color if color is not None else (randint(0,255),randint(0,255),randint(0,255))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


c1 = Circle()
c2 = Circle(x=100, y=150, r=20, color=(255, 0, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))
    c1.draw()
    c2.draw()
    pygame.display.flip()
    clock.tick(60)



pygame.quit()