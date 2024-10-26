import pytest
from unittest.mock import MagicMock
from src.landing_game_action_periodic import LandingGameActionEachFrame


def test_landing_game_action_each_frame_init():
    target_position = (300, 400)
    original_position = (1, 2)
    obj = MagicMock()
    obj.pos = original_position

    example_lambda = lambda: setattr(obj, "pos", target_position)

    periodic_action = LandingGameActionEachFrame(example_lambda)
    assert obj.pos == original_position
    periodic_action.execute_action()
    assert obj.pos == target_position


def test_landing_game_action_each_frame_invalid():
    non_lambda_object = "hello42"
    with pytest.raises(TypeError):
        LandingGameActionEachFrame(non_lambda_object)
