import pygame
from pygame.locals import *

pygame.init()

# Defining colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (242, 114, 19)
bright_orange = (252, 149, 46)

display_width = 1920
display_height = 1200

flags = DOUBLEBUF

gameDisplay = pygame.display.set_mode((display_width, display_height), flags)
pygame.display.set_caption('Heroless')

# Font for text.
font = pygame.font.SysFont(None, 50)


# Store the back of cards
backs = [pygame.image.load("img/back.png").convert_alpha(),
         pygame.image.load("img/back_01.png").convert_alpha()]

# Store backgrounds.
bgs = [pygame.image.load("img/hs.jpg").convert(),
       pygame.image.load("img/he.jpg").convert(),
       pygame.image.load("img/playground.png").convert()]

# Store cards.
cards = [pygame.image.load('img/murloc.png').convert_alpha(),
         pygame.image.load('img/bloodfen.png').convert_alpha(),
         pygame.image.load('img/tiger.png').convert_alpha(),
         pygame.image.load('img/knight_m.png').convert_alpha()]

spells = [pygame.image.load('img/rouges_do_it.png').convert_alpha()]

PC_cards = [pygame.image.load('img/shiv.png').convert_alpha(),
            pygame.image.load('img/squirrel.png').convert_alpha()]

#Written by Sentdex.
def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])