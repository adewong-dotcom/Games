import pygame

pygame.init()

i=0

clock = pygame.time.Clock()

running = True
while running:
    if i == 5:
        running = False

    clock.tick(1)
    print(clock.get_time())
    print(clock.get_fps())
    print(i)
    i += 1