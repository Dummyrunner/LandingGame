import pygame
import sys
from pygame.locals import *

from src.general_physics import meter_to_pixel
from src.game_window import GameWindow
from src.vec2d import Vec2d
from src.common_constants import CommonConstants
from src.game_timing import GameTiming
from src.scenario import Scenario
from src.scenario_overlays import ScenarioOverlays


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


def process_keyboard_events(actions_while_key_pressed, actions_on_key_down):
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.locals.KEYDOWN:
            for action in actions_on_key_down:
                if event.key == action.trigger_key.key_identifier:
                    action.execute_action()

    # check all key states and automatically perform all callbacks
    key_press_state = pygame.key.get_pressed()
    for action in actions_while_key_pressed:
        trigger_action_given: bool = (
            action.trigger_key.pressed
            == key_press_state[action.trigger_key.key_identifier]
        )
        if trigger_action_given:
            action.execute_action()


def process_each_frame_events(actions_each_frame):
    for act in actions_each_frame:
        act.execute_action()


def main():
    pygame.init()
    game_window = GameWindow("Landing Game")
    game_timing = GameTiming()
    scenario = Scenario()
    overlays = ScenarioOverlays(scenario, game_timing)

    while True:
        process_each_frame_events(scenario.actions_each_frame)
        process_keyboard_events(
            scenario.actions_while_key_pressed, scenario.actions_on_key_down
        )
        game_window.erase_screen()
        ego = scenario.object_list.get_object_by_name("ego")
        ego.kinematic.external_forces.append(
            CommonConstants.ROCKET_MASS
            * Vec2d(0, CommonConstants.GRAVITATIONAL_FORCE_EARTH)
        )
        for obj in scenario.object_list:
            obj.update(CommonConstants.TIME_STEP)
            game_window.display.blit(obj.image, obj.rect)
        for overlay in overlays.overlays:
            overlay.update()
            game_window.display.blit(overlay.image, overlay.rect)
        game_timing.update(CommonConstants.TIME_STEP)
        pygame.display.update()
        game_window.clock.tick(game_window.fps)


if __name__ == "__main__":
    main()
