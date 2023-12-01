import random
import pygame
import pygame.display
from pygame import mixer
import math

# Program Initialize
pygame.init()

# Creating a screen
screen_x = 1100
screen_y = 650
screen = pygame.display.set_mode(size=[screen_x, screen_y])

# Title, Logo
pygame.display.set_caption("Dice Simulator")
icon = pygame.image.load("images/dice.png")
pygame.display.set_icon(icon)

# Background
# backdrop = pygame.image.load("")

# Background Music
# mixer.music.load('')
# mixer.music.play(-1)

# Generates a random number between 1-6
num = random.randint(1, 6)

# X and Y Coordinates of dice
x = (screen_x/2)-64
y = (screen_y/2)-64

# Font Type, Size and Position
font = pygame.font.Font('freesansbold.ttf', 50)
textx = (screen_x/3.5)
texty = (screen_y/3.7)


# For background change
def background():
    # screen.fill((255, 255, 0))
    pass


# For Displaying Text
def text(x, y):
    start = font.render("Press the die to roll !! ", True, (255, 255, 255))
    screen.blit(start, (x, y))


# Dice image display
def dice(num, x, y):
    dice_img = f"images/dice ({num}).png"
    die = pygame.image.load(dice_img)
    screen.blit(die, (x, y))


# Detecting collision between Mouse Pointer and Dice
def iscollision(x, y, mouse_x, mouse_y):
    distance = math.sqrt((math.pow((mouse_x-(x+64)), 2)) + (math.pow((mouse_y-(y+64)), 2)))
    if distance < 80:
        return True
    else:
        return False


# Infinite Loop to execute program till it quits
running = True
while running:

    background()

    # Generates live position of mouse pointer
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    collision = iscollision(x, y, mouse_x, mouse_y)

    for event in pygame.event.get():

        # Ending the Loop when program quits
        if event.type == pygame.QUIT:
            running = False

        # Detects If Left button is click on mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                if collision:
                    num = random.randint(1, 6)

    dice(num, x, y)
    text(textx, texty)

    # Updates all changes at the time of execution
    pygame.display.update()
