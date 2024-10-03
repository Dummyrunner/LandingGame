import pygame
import sys
from pygame.locals import *

from src.game_window import GameWindow
from src.rocket import Rocket
from src.landing_game_object import LandingGameObject
from src.vec2d import Vec2d
from src.colors import colors_dict
from src.common_constants import CommonConstants, GameColors, GameFonts
from src.overlay import Overlay
from src.game_timing import GameTiming


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


def create_overlays():
    debug_overlay = Overlay(
        create_pg_surface_from_color_and_size(
            GameColors.BLACK, (CommonConstants.WINDOW_WIDTH / 3, 400)
        ),
        GameFonts.BASIC_FONT,
        128,
        (10, 10),
    )
    debug_overlay.add_line("Debug Information:")
    debug_overlay.add_line("")
    debug_overlay.add_line("Ground")
    debug_overlay.add_attribute(ground, "pos", "Altitude: ", None)

    debug_overlay.add_line("")
    debug_overlay.add_line("Rocket")
    debug_overlay.add_attribute(ego, "pos", "Position: ", None)
    debug_overlay.add_attribute(ego.kinematic, "velocity", "Velocity: ", None)
    debug_overlay.add_attribute(ego.kinematic, "acceleration", "Acceleration: ", None)

    hud_overlay = Overlay(
        create_pg_surface_from_color_and_size(
            GameColors.BLACK, (CommonConstants.WINDOW_WIDTH - 20, 80)
        ),
        GameFonts.BASIC_FONT,
        128,
        (10, CommonConstants.WINDOW_HEIGHT - 90),
    )
    hud_overlay.add_line("Time as float with 2 decimal places:")
    hud_overlay.add_attribute(game_timing, "time", "Time: ", float)
    hud_overlay.add_line("Time as int:")
    hud_overlay.add_attribute(game_timing, "time", "Time: ", int)

    rocket_label = Overlay(
        create_pg_surface_from_color_and_size(colors_dict["blue"], (40, 16)),
        GameFonts.BASIC_FONT,
        128,
        (10, 10),
    )
    rocket_label.attach_to_object(ego)
    rocket_label.add_line("Rocket")

    return debug_overlay, hud_overlay, rocket_label


pygame.init()
game_window = GameWindow("Landing Game")
game_timing = GameTiming()
rocket_pos = Vec2d(CommonConstants.WINDOW_WIDTH / 2, CommonConstants.WINDOW_HEIGHT / 2)
rocket_mass = 1e5
ground_position = Vec2d(0, 500)
img_ego = create_pg_surface_from_color_and_size(colors_dict["red"], (40, 30))
img_ground = create_pg_surface_from_color_and_size(
    colors_dict["green"], (CommonConstants.WINDOW_WIDTH, 10)
)

obj_list = pygame.sprite.Group()

ego = Rocket(img_ego, rocket_pos, rocket_mass)
ground = LandingGameObject(img_ground, ground_position)
overlays = create_overlays()

obj_list.add(ego)
obj_list.add(ground)
for overlay in overlays:
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
    game_timing.update(CommonConstants.TIME_STEP)
    pygame.display.update()
    game_window.clock.tick(game_window.fps)
