import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(10, 200, 140, 32)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('blue')

color = color_passive
active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active  # Toggle active state
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:  # Only process keys if the input is active
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    screen.fill((0, 0, 0))

    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Adjust the width of the input box based on the text
    input_rect.w = max(100, text_surface.get_width() + 10)

    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)


