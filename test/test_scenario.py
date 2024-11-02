import pytest
import pygame
from src.scenario import Scenario
from src.common_constants import CommonConstants, Opacity
from src.vec2d import Vec2d


@pytest.fixture
def scenario():
    pygame.init()
    scenario_instance = Scenario()
    yield scenario_instance
    pygame.quit()


def test_create_objects(scenario):
    object_list = scenario.object_list
    assert len(object_list) == 3

    ego = object_list.get_object_by_name("ego")
    assert ego is not None
    assert isinstance(ego, pygame.sprite.Sprite)
    assert ego.rect.center == (
        CommonConstants.WINDOW_WIDTH / 2,
        CommonConstants.WINDOW_HEIGHT / 2,
    )

    ground = object_list.get_object_by_name("ground")
    assert ground is not None
    assert isinstance(ground, pygame.sprite.Sprite)
    assert ground.rect.center == (CommonConstants.WINDOW_WIDTH / 2, 500)

    ego_engine_fire = object_list.get_object_by_name("ego_engine_fire")
    assert ego_engine_fire is not None
    assert isinstance(ego_engine_fire, pygame.sprite.Sprite)
    assert ego_engine_fire.rect.center == (
        ego.rect.midbottom[0],
        ego.rect.midbottom[1] + 0.5 * CommonConstants.EXHAUST_FIRE_DOWN_DIMENSIONS.y,
    )


def test_create_actions(scenario):
    action_dict = scenario.action_dict
    assert "activate_ego_upwards_boost" in action_dict
    assert "activate_left_engine_boost" in action_dict
    assert "activate_right_engine_boost" in action_dict
    assert "hide_engine_fire_up" in action_dict
    assert "show_engine_fire_up" in action_dict
    assert "glue_engine_fire_down_to_ego" in action_dict


def test_create_key_bindings(scenario):
    actions_each_frame, actions_while_key_pressed, actions_on_key_down = (
        scenario.create_key_bindings(scenario.action_dict)
    )

    assert len(actions_each_frame) == 1
    assert len(actions_while_key_pressed) == 5
    assert len(actions_on_key_down) == 0


def test_ego_upwards_boost(scenario):
    ego = scenario.object_list.get_object_by_name("ego")
    initial_force_count = len(ego.kinematic.external_forces)
    scenario.action_dict["activate_ego_upwards_boost"]()
    assert len(ego.kinematic.external_forces) == initial_force_count + 1


def test_left_engine_boost(scenario):
    ego = scenario.object_list.get_object_by_name("ego")
    initial_force_count = len(ego.kinematic.external_forces)
    scenario.action_dict["activate_left_engine_boost"]()
    assert len(ego.kinematic.external_forces) == initial_force_count + 1


def test_right_engine_boost(scenario):
    ego = scenario.object_list.get_object_by_name("ego")
    initial_force_count = len(ego.kinematic.external_forces)
    scenario.action_dict["activate_right_engine_boost"]()
    assert len(ego.kinematic.external_forces) == initial_force_count + 1


def test_show_hide_engine_fire(scenario):
    ego_engine_fire = scenario.object_list.get_object_by_name("ego_engine_fire")
    scenario.action_dict["show_engine_fire_up"]()
    assert ego_engine_fire.image.get_alpha() == Opacity.OPAQUE
    scenario.action_dict["hide_engine_fire_up"]()
    assert ego_engine_fire.image.get_alpha() == Opacity.TRANSPARENT
