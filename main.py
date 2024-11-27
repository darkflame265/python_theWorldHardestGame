from Settings import *
from tiles import Tile
from levels import Level
import pygame
import random
import time
import sys


pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(Tile((100, 100), 200))
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    #test_tile.draw(screen)
    level.run()

    pygame.display.update()
    clock.tick(60)