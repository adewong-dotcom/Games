from turtle import back
import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.gunshot = pygame.mixer.Sound("gunshot.wav")
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_sprites, True)

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

#General setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprites")
background = pygame.image.load("BG.png")
background = pygame.transform.scale(background, (800, 500))
pygame.mouse.set_visible(False)

crosshair = Crosshair(20, 20, "crosshair.png")
player_group = pygame.sprite.Group()
player_group.add(crosshair)

target_sprites = pygame.sprite.Group()
for target in range(50):
    new_target = Target("target.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_sprites.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    #Drawing
    screen.blit(background, (0, 0))
    target_sprites.draw(screen)
    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()
    clock.tick(30)

#To close elegantly    
pygame.quit()
sys.exit()