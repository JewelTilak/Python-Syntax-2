import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(RED)  
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 680)  
        self.rect.y = random.randrange(0, 350)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 255, 0))  
        self.rect = self.image.get_rect()
        self.rect.y = 370

    def update(self):
        
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)  
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.y -= 3
        
        if self.rect.y < -10:
            self.kill()  


pygame.init()

# Set the dimensions of the window
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Create sprite groups
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

# Create blocks
for i in range(50):
    block = Block()
    block_list.add(block)
    all_sprites_list.add(block)

# Create player
player = Player()
all_sprites_list.add(player)

done = False
clock = pygame.time.Clock()
score = 0

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = Bullet()
            bullet.rect.x = player.rect.x + 8  # Center bullet under player
            bullet.rect.y = player.rect.y
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # Update all sprites
    all_sprites_list.update()

    # Check for bullet collisions with blocks
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # If a bullet hits a block
        if block_hit_list:
            score += len(block_hit_list)  # Increase score by number of blocks hit
            bullet.kill()  # Remove bullet

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_surface = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()

