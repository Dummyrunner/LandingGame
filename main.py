import pygame
from pygame.locals import *

from src.general_physics import meter_to_pixel
from src.game_window import GameWindow
from src.vec2d import Vec2d
from src.common_constants import CommonConstants
from src.game_timing import GameTiming
from src.scenario import Scenario
from src.scenario_overlays import ScenarioOverlays
from src.event_handler import EventHandler


def main():
    pygame.init()
    game_window = GameWindow("Landing Game")
    game_timing = GameTiming()
    scenario = Scenario()
    overlays = ScenarioOverlays(scenario, game_timing)
    event_handler = EventHandler()

    while True:
        event_handler.process_events(
            scenario.actions_each_frame,
            scenario.actions_while_key_pressed,
            scenario.actions_on_key_down,
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
