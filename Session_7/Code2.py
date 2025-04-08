import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()


class Ball:
    def __init__(self):
        self.x = randint(-50,500)
        self.y = randint(-50,500)
        self.r = randint(5,25)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.x_speed = randint(-2,5)
        self.y_speed = randint(-2,5)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def rebound(self):
        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = self.x_speed * -1
        if self.y - self.r < 0  or self.y + self.r > 500:
            self.y_speed = self.y_speed * -1



class fastBall(Ball):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_speed*2
        self.y += self.y_speed*2

    def rebound(self):
        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = self.x_speed * -1
        if self.y - self.r < 0  or self.y + self.r > 500:
            self.y_speed = self.y_speed * -1



class slowBall(Ball):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def rebound(self):
        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = self.x_speed * -1
        if self.y - self.r < 0  or self.y + self.r > 500:
            self.y_speed = self.y_speed * -1

c1 = Ball()
c2 = fastBall()
c3 = slowBall()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255,255,255))
    c1.draw()
    c1.move()
    c1.rebound()

    c2.draw()
    c2.move()
    c2.rebound()

    c3.draw()
    c3.move()
    c3.rebound()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
