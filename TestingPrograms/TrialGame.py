import pygame
from pygame.locals import *

#Color variables
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.font.init()

def create_font(t, s=72, color=YELLOW, b= False, i= False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic = i)
    text = font.render(t, True, color)
    return text

game_over = create_font("GAME OVER")
restart = create_font("Press Space to restart", 36, (9, 0, 180))

size = 600, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

loop = True
press = False
while loop:
    try:
        screen.fill((0, 0, 0))
        px, py = pygame.mouse.get_pos()
        screen.blit(game_over, (100, 150))
        screen.blit(restart, (10, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        pygame.display.update()
        clock.tick(60)
    except Exception as e:
        print(e)
        pygame.quit()

pygame.quit()