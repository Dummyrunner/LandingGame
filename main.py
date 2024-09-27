import pygame
import sys
from pygame.locals import *

from src.game_window import GameWindow
from src.rocket import Rocket
from src.landing_site import LandingSite
from src.vec2d import Vec2d
from src.colors import colors_dict
from src.common_constants import CommonConstants

pygame.init()
game_window = GameWindow("Landing Game")
rocket_pos = Vec2d(CommonConstants.WINDOW_WIDTH / 2, CommonConstants.WINDOW_HEIGHT / 2)
rocket_mass = 1e5
img = pygame.Surface((40, 30))
img.fill(colors_dict["red"])

ego = Rocket(img, rocket_pos, rocket_mass)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    game_window.erase_screen()
    ego.update(CommonConstants.TIME_STEP)
    game_window.display.blit(ego.image, ego.rect)
    pygame.display.update()
    game_window.clock.tick(game_window.fps)
