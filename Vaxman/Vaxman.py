#Importing pygame, random and keys that will be used in gameplay
import pygame, random, sys

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

#Constant variables for width and height
WIDTH = 606
HEIGHT = 606

#Constant variables for colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (47, 86, 233)
ORANGE = (255, 173, 47)
PINK = (255, 47, 154)
GREEN = (169, 255, 47)
WHITE = (255, 255, 255)
LIGHT_BLUE = (52, 204, 255)

#Creates the events to create enemies
ADDENEMY = pygame.USEREVENT + 1

# Starts pygame and font
pygame.init()
pygame.font.init()

#Method to create font
def create_font(t, s=32, c=(255, 255, 255), b=False, i=False):
    font = pygame.font.SysFont("KdamThmorPro-Regular.ttf", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text

#Player class for VaxMan
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        img = pygame.image.load("Vaxman.png")
        img = pygame.transform.scale(img, (50, 50))
        self.surf = img.convert()
        self.surf.set_colorkey(BLACK, RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 5
    
    def update(self, pressed_keys):
        #self.rect.move_ip(self.speed, self.speed)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = WIDTH
        if self.rect.right > WIDTH:
            self.rect.right = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color=PINK):
        super(Enemy, self).__init__()
        #image = pygame.image.load("fantom.png")
        #self.image = pygame.transform.scale(image, (40, 40))
        image = pygame.draw.circle(screen, color)
        self.surf.set_colorkey(BLACK, RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(WIDTH +20, WIDTH + 100),
                random.randint(0, HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self, pressed_keys):
        #self.rect.move_ip(self.speed, self.speed)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = WIDTH
        if self.rect.right > WIDTH:
            self.rect.right = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Wall(pygame.sprite.Sprite):
    #Constructor function
    def __init__(self, x, y, width, height, color=BLUE):
        super().__init__(self)

        #Makes a blue wall of the size specified in the parameters
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(color)

        #Makes our top-left corner the passed in location
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.top = x

#Creates all the walls in Room 1
def setupRoomOne(all_sprites_list):
    #Make the walls. (x_pos, y_pos, width, height)
    wall_list = pygame.sprite.RenderPlain()

    #This is a list of walls. Each is in the form [x, y, width, height]
    walls = [   [0, 0, 6, 600],
                [0, 0, 600, 6],
                [0, 600, 606, 6],
                [600, 0, 6, 606],
                [300, 0, 6, 66],
                [60, 60, 186, 6],
                [360, 60, 186, 6],
                [60, 120, 66, 6],
                [60, 120, 6, 126],
                [180, 120, 246, 6],
                [300, 120, 6, 66],
                [480, 120, 66, 6],
                [540, 120, 6, 126],
                [120, 180, 126, 6],
                [120, 180, 6, 126],
                [360, 180, 126, 6],
                [480, 180, 6, 126],
                [180, 240, 6, 126],
                [180, 360, 246, 6],
                [420, 240, 6, 126],
                [240, 240, 42, 6],
                [324, 240, 42, 6],
                [240, 240, 6, 66],
                [240, 300, 126, 6],
                [360, 240, 6, 66],
                [0, 300, 66, 6],
                [540, 300, 66, 6],
                [60, 360, 66, 6],
                [60, 360, 6, 186],
                [480, 360, 66, 6],
                [540, 360, 6, 186],
                [120, 420, 366, 6],
                [120, 420, 6, 66],
                [480, 420, 6, 66],
                [180, 480, 246, 6],
                [300, 480, 6, 66],
                [120, 540, 126, 6],
                [360, 540, 126, 6]
            ]
    #Loops through the list. Creates the wall and adds it to the list
    for item in walls:
        wall = Wall(item[0], item[1], item[2], item[3])
        wall_list.add(wall)
        all_sprites_list.add(wall)

    return wall_list
#Instantiates player, enemy, clock, and walls
player = Player()
enemy = Enemy()
clock = pygame.time.Clock()

#Sets screen parameters
screen = pygame.display.set_mode([WIDTH, HEIGHT])


# Main loop with gameplay
running = True

while running:
    
    #Iterates through even queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #Checks for Base Case 1 where Excape is pressed
            if event.type == K_ESCAPE:
                running = False
        #Checks if the window was closed    
        elif event.type == QUIT:
            running = False

    screen.fill(BLACK)
    
    #flips the display
    pygame.display.flip()

#To make sure it quits
pygame.quit()
