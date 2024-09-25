import pygame
import sys
from pygame.locals import *

from src.game_window import GameWindow
from src.rocket import Rocket
from src.landing_site import LandingSite
from src.colors import colors_dict
from src.common_constants import CommonConstants

pygame.init()
game_window = GameWindow("Landing Game")

rocket = Rocket(
    600, 100, 50, 50, colors_dict["red"], 0, 0
)  # TODO find out, why the rocket is not displayed correctly
ground = LandingSite(200, 200, 100, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    game_window.erase_screen()
    ground.draw(game_window.display)
    rocket.draw(game_window.display)
    pygame.display.update()
    game_window.clock.tick(game_window.fps)
