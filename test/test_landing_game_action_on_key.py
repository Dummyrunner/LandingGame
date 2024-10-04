import pygame
from typing import Type
from enum import Enum
import pytest
from src.landing_game_action_on_key import PygameKeyState, LandingGameActionOnKey

TEST_MSG = "hello i am the test callback function"


def is_enum_value(enum_class: Type[Enum], value: int) -> bool:
    return any(member.value == value for member in enum_class)


def test_pygame_key_state_init_valid():
    example_pressed = True
    example_key_identifier = pygame.K_SPACE
    PygameKeyState(example_key_identifier, example_pressed)


def test_pygame_key_state_invalid_pressed():
    invalid_example_pressed = "non-boolean-object"
    example_key_identifier = pygame.K_SPACE
    with pytest.raises(TypeError):
        PygameKeyState(example_key_identifier, invalid_example_pressed)


@pytest.fixture
def valid_example_landing_game_action_on_key():
    example_key = pygame.K_SPACE
    example_key_state = PygameKeyState(example_key, False)
    example_callback = lambda: print(TEST_MSG)
    return LandingGameActionOnKey(example_key_state, example_callback)


def test_landing_game_action_on_key_init_valid(
    valid_example_landing_game_action_on_key,
):
    assert type(valid_example_landing_game_action_on_key) == LandingGameActionOnKey


def test_landing_game_action_on_key_execute_action(
    valid_example_landing_game_action_on_key, capsys
):
    obj = valid_example_landing_game_action_on_key
    obj.execute_action()
    captured_output = capsys.readouterr().out
    assert captured_output.strip() == TEST_MSG
