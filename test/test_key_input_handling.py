import pytest
import pygame
from pygame.locals import *
from src.game_window import GameWindow
from src.landing_game_object import LandingGameObject
from src.vec2d import Vec2d
from src.colors import colors_dict
from src.common_constants import CommonConstants
from src.game_timing import GameTiming
from src.landing_game_action_on_key import PygameKeyState, LandingGameActionOnKey


def create_pg_surface_from_color_and_size(color, size):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf


def process_key_pressed_events(actions_while_key_pressed, key_pressed_list):
    """check all key states on key pressed and automatically perform all callbacks on them"""
    for action in actions_while_key_pressed:
        trigger_action_given: bool = (
            action.trigger_key.pressed
            == key_pressed_list[action.trigger_key.key_identifier]
        )
        if trigger_action_given:
            action.execute_action()


def mocked_no_key_pressed():
    tmp = [0] * 300
    return tmp


def mocked_one_key_pressed(pressed_key):
    tmp = [0] * 300
    tmp[pressed_key] = 1
    return tmp


EXPECTED_COLOR_SPACEKEY_UP = colors_dict["blue"]
EXPECTED_COLOR_SPACEKEY_DOWN = colors_dict["cyan"]


@pytest.mark.parametrize(
    "keys_down_list,expected_color",
    [
        (mocked_no_key_pressed(), EXPECTED_COLOR_SPACEKEY_UP),
        (mocked_one_key_pressed(pygame.K_SPACE), EXPECTED_COLOR_SPACEKEY_DOWN),
    ],
)
def test_key_input_pressed_handling(keys_down_list, expected_color):
    """Setup LandingGameAction that changes object color while key is down and check this"""
    pygame.init()

    game_window = GameWindow("Landing Game")
    game_timing = GameTiming()

    img_key_indicator_while_pressed = create_pg_surface_from_color_and_size(
        colors_dict["red"], (20, 20)
    )

    key_indicator_while_pressed = LandingGameObject(
        0,
        img_key_indicator_while_pressed,
        Vec2d(CommonConstants.WINDOW_WIDTH - 50, CommonConstants.WINDOW_HEIGHT - 50),
    )
    coordinate_inside_key_inidicator = key_indicator_while_pressed.pos + Vec2d(1, 1)

    # predefine actions on key: keypress-states connected to actions that will be performed if state is given
    color_key_indicator_blue_pressed = lambda: key_indicator_while_pressed.set_color(
        EXPECTED_COLOR_SPACEKEY_DOWN
    )
    color_key_indicator_cyan_pressed = lambda: key_indicator_while_pressed.set_color(
        EXPECTED_COLOR_SPACEKEY_UP
    )

    act_change_box_color_while_spacebar_pressed = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, True), color_key_indicator_blue_pressed
    )
    act_change_box_color_while_spacebar_not_pressed = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, False), color_key_indicator_cyan_pressed
    )

    obj_list = pygame.sprite.Group()
    obj_list.add(key_indicator_while_pressed)

    # bundle all keystate -> action correlations into one list
    actions_while_key_pressed = [
        act_change_box_color_while_spacebar_pressed,
        act_change_box_color_while_spacebar_not_pressed,
    ]

    pygame.event.pump()
    process_key_pressed_events(actions_while_key_pressed, keys_down_list)
    game_window.erase_screen()
    for obj in obj_list:
        obj.update(CommonConstants.TIME_STEP)
        game_window.display.blit(obj.image, obj.rect)
    assert (
        game_window.display.get_at(coordinate_inside_key_inidicator) == expected_color
    )
    game_timing.update(CommonConstants.TIME_STEP)
    pygame.display.update()
    game_window.clock.tick(game_window.fps)
