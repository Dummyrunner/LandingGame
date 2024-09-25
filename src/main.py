import pygame
import sys
from pygame.locals import *
from game_window import GameWindow

pygame.init()
game_window = GameWindow("Game Window")

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
