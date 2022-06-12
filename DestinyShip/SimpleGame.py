#Simple pygame program

# Import the pygame library and random for random numbers
import pygame
import random

#Import pygame.locals for easier access to key coordinates
#Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#Define a Player object by extending pygame.sprite.Sprite
#The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        picture = pygame.image.load("jet.png")
        picture = pygame.transform.scale(picture, (96, 54))
        self.surf = picture.convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        #K_UP, K_DOWN, K_LEFT, K_RIGHT correspond to the arrow keys on the keyboard
        #self.rect.mo_ip(x, y) defines how much the rect/Player should be moved
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        #Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH_SCREEN:
            self.rect.right = WIDTH_SCREEN
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT_SCREEN:
            self.rect.bottom = HEIGHT_SCREEN

#Defines the enemy object by extending pygame.sprite.Sprite
#The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        picture2 = pygame.image.load("missile.png")
        picture2 = pygame.transform.scale(picture2, (48, 27))
        self.surf = picture2.convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        #The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH_SCREEN + 20, WIDTH_SCREEN + 100),
                random.randint(0, HEIGHT_SCREEN),
            )
        )
        self.speed = random.randint(5, 20)
    
    #Move the sprite based on speed
    #Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#Define the cloud object by extending pygame.sprite.Sprite
#Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        bk_picture = pygame.image.load("cloud.png")
        bk_picture = pygame.transform.scale(bk_picture, (96, 54))
        self.surf = bk_picture.convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        #The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(WIDTH_SCREEN + 20, WIDTH_SCREEN + 100),
                random.randint(0, HEIGHT_SCREEN),
            )
        )

    #Move the cloud based on a constant speed
    #Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Initialize the pygame library
pygame.init()

#Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Set up the drawing window and its constants
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 600
screen = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])

#Creates a custom event for adding a new enemy
#Events are added as integers to add an event you need to define it as
#a unique integer. USEREVENT is the last event reserved by pygame so adding
# 1 makes sure that it is unique
ADDENEMY = pygame.USEREVENT + 1
#the following line inserts this new event every 250 milliseconds or four times per second
#pygame.time.set_timer(int event, int milliseconds)
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

#Instantiate player. Right now, this is just a rectangle.
player = Player()

#Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:

    #Did the user click the window close button
    for event in pygame.event.get():
        #Did the user hit a key?
        if event.type == KEYDOWN:
            #Was it the Escape key? If so, stop the loop.
            if event.type == K_ESCAPE:
                running = False

        #Did the user click the window close button? If so stop the loop.
        elif event.type == QUIT:
            running = False

        #Add a new enemy?
        elif event.type == ADDENEMY:
            #Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        #Add a new cloud?
        elif event.type == ADDCLOUD:
            #Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    #Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    #Update the player sprite based on user keypresses
    player.update(pressed_keys)

    #Update enemy position and clouds
    enemies.update()
    clouds.update()

    #Fill the background with sky blue
    screen.fill((135, 206, 250))

    #Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    #Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        #If so, then remove the player and stop the loop
        player.kill()
        running = False

    #Create a surface and pass in a tuple containing its length and width
    #surf = pygame.Surface((50, 50))

    #Give the surface a color to separate it from the background
    # surf.fill((0, 0, 0))
    #rect = surf.get_rect()

    #Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (WIDTH_SCREEN/2, HEIGHT_SCREEN/2), 75)

    #Calls blit that stands for Block Transfer that basically
    #transfers the content of a Surface onto another Surface
    #Keep in mind that blit will place the surface at the top-left corner of surf
    #at the location given
    #surf_center = (
    #    (WIDTH_SCREEN - surf.get_width())/2,
    #    (HEIGHT_SCREEN - surf.get_height())/2
    #)
    #screen.blit(surf, surf_center)

    #Draw the player on the screen
    #Removed since it is already included in the for loop above
    #screen.blit(player.surf, player.rect)

    #Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
pygame.quit()