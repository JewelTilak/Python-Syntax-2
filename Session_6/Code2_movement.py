import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x = None, y = None, r = None, color = None, x_speed = None, y_speed = None):
        self.x = x if x is not None else randint(-50,500)
        self.y = y if y is not None else randint(-50,500)
        self.r = r if r is not None else randint(0, 10)
        self.color = color if color is not None else (randint(0,255),randint(0,255),randint(0,255))
        self.x_speed = x_speed if x_speed is not None else randint(-2,10)
        self.y_speed = y_speed if y_speed is not None else randint(-2,10)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        if self.x - self.r < 0 or self.r + self.x > 500:
            self.x_speed = -self.x_speed
        if self.y - self.r < 0 or self.r + self.y > 500:
            self.y_speed = -self.y_speed



c1 = Circle()
c2 = Circle(x=100, y=150, r=10, color=(255, 0, 0), x_speed = 1, y_speed = 2)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255,255,255))
    c1.draw()
    c1.move()
    c2.draw()
    c2.move()
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()


