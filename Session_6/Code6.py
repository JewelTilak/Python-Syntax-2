import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)
user_text = ''

input_rect = pygame.Rect(10, 200, 200, 32)

active_color = pygame.Color('lightskyblue3')
passive_color = pygame.Color('chartreuse4')

color = passive_color
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    screen.fill((255, 255, 255))

    
    color = active_color if active else passive_color
    pygame.draw.rect(screen, color, input_rect, 2)

    text_surface = base_font.render(user_text, True, (0, 0, 0))


    if text_surface.get_width() > input_rect.width - 10:
        offset = text_surface.get_width() - (input_rect.width - 10)
    else:
        offset = 0

    screen.blit(text_surface, (input_rect.x + 5 - offset, input_rect.y + 5))
    input_rect.width = max(100, text_surface.get_width() + 10)
    pygame.display.flip()

    clock.tick(60)
