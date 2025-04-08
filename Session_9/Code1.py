import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0), (250,250), 25)
    pygame.display.flip()

pygame.quit()