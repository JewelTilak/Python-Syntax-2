import pygame
import sys
from random import randint


pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x = None, y = None, r = None, color = None, x_speed = None, y_speed = None):
        self.x = x if x is not None else randint(-50,500)
        self.y = y if y is not None else randint(-50, 500)
        self.r = r if r is not None else randint(5,20)
        self.color = color if color is not None else (randint(0,255),randint(0,255),randint(0,255))
        self.x_speed = x_speed if x_speed is not None else randint(-2,2)
        self.y_speed = y_speed if y_speed is not None else randint(-2,2)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.r)

    def move(self):
        self.x += self.x_speed * 4
        self.y += self.y_speed * 4

        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = -self.x_speed
        if self.y - self.r < 0 or self.y + self.r > 500:
            self.y_speed = self.y_speed


class FastBall(Circle):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.r)

    def move(self):
        self.x += self.x_speed * 3
        self.y += self.y_speed * 3

        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = -self.x_speed
        if self.y - self.r < 0 or self.y + self.r > 500:
            self.y_speed = -self.y_speed


class SlowBall(Circle):
    def __init__(self):
        super().__init__()

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y),self.r)

    def move(self):
        self.x += self.x_speed *1.5
        self.y += self.y_speed *1.5

        if self.x - self.r < 0 or self.x + self.r > 500:
            self.x_speed = -self.x_speed
        if self.y - self.r < 0 or self.y + self.r > 500:
            self.y_speed = -self.y_speed



c1 = FastBall()
c2 = SlowBall()
# c3 = Circle(x = 150, y = 180, r = 10, color = (0,0,0), x_speed = 5, y_speed = 5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    c1.draw()
    c2.draw()
    c1.move()
    c2.move()
    # c3.draw()
    # c3.move()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()






