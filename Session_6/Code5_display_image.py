import pygame
pygame.init()

x = 600
y = 600

screen = pygame.display.set_mode([x, y])
pygame.display.set_caption("Image")

img = pygame.image.load('Session_6\matrix.png').convert()
screen.blit(img, (0,0))
pygame.display.flip()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()


