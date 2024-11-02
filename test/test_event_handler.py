import pytest
import pygame

from src.event_handler import EventHandler
from src.landing_game_action_periodic import LandingGameActionEachFrame
from src.landing_game_action_on_key import LandingGameActionOnKey, PygameKeyState
from unittest.mock import MagicMock, patch


@pytest.fixture
def handle_events():
    pygame.init()
    handle_events = EventHandler()
    return EventHandler()


def test_process_events():
    assert handle_events is not None


def test_process_each_frame_events(handle_events):
    actions_each_frame = [
        LandingGameActionEachFrame(MagicMock(lambda: MagicMock())),
        LandingGameActionEachFrame(MagicMock(lambda: MagicMock())),
    ]
    handle_events._EventHandler__process_each_frame_events(actions_each_frame)
    assert actions_each_frame[0].action_callback.call_count == 1
    assert actions_each_frame[1].action_callback.call_count == 1


def test_process_keyboard_events_on_key_down(handle_events):
    action_on_key_down = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, True), lambda: MagicMock()
    )
    actions_on_key_down = [action_on_key_down]

    with patch(
        "pygame.event.get",
        return_value=[MagicMock(type=pygame.KEYDOWN, key=pygame.K_SPACE)],
    ):
        handle_events._EventHandler__process_keyboard_events([], actions_on_key_down)


def test_process_keyboard_events_while_key_pressed(handle_events):
    action_while_key_pressed = LandingGameActionOnKey(
        PygameKeyState(pygame.K_SPACE, True), MagicMock(lambda: MagicMock())
    )
    actions_while_key_pressed = [action_while_key_pressed]

    with patch("pygame.key.get_pressed", return_value={pygame.K_SPACE: True}):
        handle_events._EventHandler__process_keyboard_events(
            actions_while_key_pressed, []
        )
        assert action_while_key_pressed.action_callback.call_count == 1
