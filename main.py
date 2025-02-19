import pygame
from pygame.locals import *

from src.general_physics import objects_collide, apply_vertical_collision_damage
from src.game_window import GameWindow
from src.vec2d import Vec2d
from src.common_constants import CommonConstants
from src.game_timing import GameTiming
from src.scenario import Scenario
from src.scenario_overlays import ScenarioOverlays
from src.event_handler import EventHandler
from src.scenario_termination import ScenarioTermination
from src.scenario_results_struct import ScenarioState


def main():
    pygame.init()
    game_window = GameWindow("Landing Game")
    game_timing = GameTiming()
    scenario = Scenario()
    overlays = ScenarioOverlays(scenario, game_timing)
    event_handler = EventHandler()
    scenario.termination_condition = lambda: objects_collide(
        scenario.object_list.get_object_by_name("ego"),
        scenario.object_list.get_object_by_name("ground"),
    )

    scenario_termination = ScenarioTermination(scenario)

    while not scenario.termination_condition():
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
        ground = scenario.object_list.get_object_by_name("ground")
        if objects_collide(ego, ground):
            apply_vertical_collision_damage(ego, ground)
        game_timing.update(CommonConstants.TIME_STEP)
        pygame.display.update()
        game_window.clock.tick(game_window.fps)

    final_elapsed_time = game_timing.time
    scenario_termination.assign_values_to_scenario_result_struct(
        ScenarioState.SUCCESS, final_elapsed_time, ego.health
    )
    result_struct = scenario_termination.result_dict
    scenario_termination.execute_termination()


if __name__ == "__main__":
    main()
