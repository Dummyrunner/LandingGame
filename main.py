import pygame
import sys
from pygame.locals import *

from src.game_window import GameWindow
from src.rocket import Rocket
from src.landing_game_object import LandingGameObject
from src.vec2d import Vec2d
from src.colors import colors_dict
from src.common_constants import CommonConstants
from src.overlay import Overlay


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


pygame.init()
game_window = GameWindow("Landing Game")
rocket_pos = Vec2d(CommonConstants.WINDOW_WIDTH / 2, CommonConstants.WINDOW_HEIGHT / 2)
rocket_mass = 1e5
ground_position = Vec2d(0, 500)
img_ego = create_pg_surface_from_color_and_size(colors_dict["red"], (40, 30))
img_ground = create_pg_surface_from_color_and_size(
    colors_dict["green"], (CommonConstants.WINDOW_WIDTH, 10)
)

ego = Rocket(img_ego, rocket_pos, rocket_mass)
ground = LandingGameObject(img_ground, ground_position)

obj_list = pygame.sprite.Group()

obj_list.add(ego)
obj_list.add(ground)
overlay = Overlay(
    create_pg_surface_from_color_and_size(
        colors_dict["black"],
        (CommonConstants.WINDOW_WIDTH, CommonConstants.WINDOW_HEIGHT),
    ),
    (0, 0),
    obj_list,
)
obj_list.add(overlay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    game_window.erase_screen()
    for i, obj in enumerate(obj_list):
        obj.update(CommonConstants.TIME_STEP)
        game_window.display.blit(obj.image, obj.rect)
    pygame.display.update()
    game_window.clock.tick(game_window.fps)
