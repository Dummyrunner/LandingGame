import pygame
import sys
from pygame.locals import *

from src.general_physics import meter_to_pixel
from src.game_window import GameWindow
from src.rocket import Rocket
from src.landing_game_object import LandingGameObject
from src.vec2d import Vec2d
from src.colors import colors_dict
from src.common_constants import CommonConstants, GameFonts, Opacity
from src.overlay import Overlay
from src.game_timing import GameTiming
from src.landing_game_action_on_key import PygameKeyState, LandingGameActionOnKey


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


def create_overlays(ground, ego, game_timing):
    debug_overlay = Overlay(
        create_pg_surface_from_color_and_size(
            colors_dict["black"], (CommonConstants.WINDOW_WIDTH / 3, 400)
        ),
        GameFonts.BASIC_FONT,
        (10, 10),
        Opacity.SEMI_TRANSPARENT,
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
            colors_dict["black"], (CommonConstants.WINDOW_WIDTH - 20, 80)
        ),
        GameFonts.BASIC_FONT,
        (10, CommonConstants.WINDOW_HEIGHT - 90),
        Opacity.SEMI_TRANSPARENT,
    )
    hud_overlay.add_line("Time as float with 2 decimal places:")
    hud_overlay.add_attribute(game_timing, "time", "Time: ", float)
    hud_overlay.add_line("Time as int:")
    hud_overlay.add_attribute(game_timing, "time", "Time: ", int)

    return [debug_overlay, hud_overlay]


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


def main():
    pygame.init()
    game_window = GameWindow("Landing Game")
    game_timing = GameTiming()
    rocket_pos = Vec2d(
        CommonConstants.WINDOW_WIDTH / 2, CommonConstants.WINDOW_HEIGHT / 2
    )
    rocket_mass = CommonConstants.ROCKET_MASS
    ground_position = Vec2d(CommonConstants.WINDOW_WIDTH / 2, 500)
    img_ego = create_pg_surface_from_color_and_size(
        colors_dict["red"],
        (meter_to_pixel(3.0), meter_to_pixel(8.0)),
    )
    img_ground = create_pg_surface_from_color_and_size(
        colors_dict["green"], (CommonConstants.WINDOW_WIDTH, 10)
    )

    img_key_indicator_while_pressed = create_pg_surface_from_color_and_size(
        colors_dict["cyan"], (20, 20)
    )

    key_indicator_while_pressed = LandingGameObject(
        img_key_indicator_while_pressed,
        Vec2d(CommonConstants.WINDOW_WIDTH - 50, CommonConstants.WINDOW_HEIGHT - 50),
    )
    img_key_indicator_on_down = create_pg_surface_from_color_and_size(
        colors_dict["cyan"], (20, 20)
    )

    key_indicator_on_down = LandingGameObject(
        img_key_indicator_on_down,
        Vec2d(CommonConstants.WINDOW_WIDTH - 100, CommonConstants.WINDOW_HEIGHT - 50),
    )

    ego = Rocket(img_ego, rocket_pos, rocket_mass)
    ground = LandingGameObject(img_ground, ground_position)
    overlays = create_overlays(ground, ego, game_timing)

    # predefine actions on key: keypress-states connected to actions that will be performed if state is given
    color_key_indicator_blue_while_pressed = (
        lambda: key_indicator_while_pressed.set_color(colors_dict["blue"])
    )
    color_key_indicator_cyan_while_pressed = (
        lambda: key_indicator_while_pressed.set_color(colors_dict["cyan"])
    )

    color_key_indicator_blue_on_down = lambda: key_indicator_on_down.set_color(
        colors_dict["blue"]
    )

    toggle_overlay_visibility_on_down = lambda: overlays[0].toggle_visibility()

    activate_ego_upwards_boost = lambda: ego.kinematic.external_forces.append(
        CommonConstants.ROCKET_UPWARD_BOOST_FORCE_SCALAR * Vec2d(0, -1)
    )
    activate_left_engine_boost = lambda: ego.kinematic.external_forces.append(
        CommonConstants.ROCKET_SIDEWAYS_BOOST_FORCE_SCALAR * Vec2d(-1, 0)
    )
    activate_right_engine_boost = lambda: ego.kinematic.external_forces.append(
        CommonConstants.ROCKET_SIDEWAYS_BOOST_FORCE_SCALAR * Vec2d(1, 0)
    )

    act_change_box_color_while_spacebar_pressed = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, True), color_key_indicator_blue_while_pressed
    )
    act_change_box_color_while_spacebar_not_pressed = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, False), color_key_indicator_cyan_while_pressed
    )

    act_change_box_color_on_spacebar_down = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, True), color_key_indicator_blue_on_down
    )

    act_toggle_overlay_visibility_on_v_down = LandingGameActionOnKey(
        PygameKeyState(pygame.K_v, True), toggle_overlay_visibility_on_down
    )

    act_boost_ego_up_on_upwards_key = LandingGameActionOnKey(
        PygameKeyState(pygame.K_UP, True), activate_ego_upwards_boost
    )
    act_boost_ego_left_on_left_key = LandingGameActionOnKey(
        PygameKeyState(pygame.K_LEFT, True), activate_left_engine_boost
    )
    act_boost_ego_up_on_rigth_key = LandingGameActionOnKey(
        PygameKeyState(pygame.K_RIGHT, True), activate_right_engine_boost
    )

    obj_list = pygame.sprite.Group()
    obj_list.add(key_indicator_while_pressed)
    obj_list.add(key_indicator_on_down)
    obj_list.add(ego)
    obj_list.add(ground)
    for overlay in overlays:
        obj_list.add(overlay)

    # bundle all keystate -> action correlations into one list
    actions_while_key_pressed = [
        act_change_box_color_while_spacebar_pressed,
        act_change_box_color_while_spacebar_not_pressed,
        act_boost_ego_up_on_upwards_key,
        act_boost_ego_left_on_left_key,
        act_boost_ego_up_on_rigth_key,
    ]
    actions_on_key_down = [
        act_change_box_color_on_spacebar_down,
        act_toggle_overlay_visibility_on_v_down,
    ]

    while True:
        process_keyboard_events(actions_while_key_pressed, actions_on_key_down)
        game_window.erase_screen()
        ego.kinematic.external_forces.append(
            CommonConstants.ROCKET_MASS
            * Vec2d(0, CommonConstants.GRAVITATIONAL_FORCE_EARTH)
        )
        for i, obj in enumerate(obj_list):
            obj.update(CommonConstants.TIME_STEP)
            game_window.display.blit(obj.image, obj.rect)
        game_timing.update(CommonConstants.TIME_STEP)
        pygame.display.update()
        game_window.clock.tick(game_window.fps)


if __name__ == "__main__":
    main()
