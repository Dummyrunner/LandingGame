import pytest
import pygame
from src.overlay import Overlay
from src.game_statistics import GameStatistics
from src.landing_game_object import LandingGameObject


@pytest.fixture
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def sample_image():
    return pygame.Surface((200, 100))


@pytest.fixture
def sample_position():
    return (10, 10)


@pytest.fixture
def sample_objects_to_display():
    return {"time_in_seconds": 100, "floattine": 3.14}


@pytest.fixture
def overlay(sample_image, sample_position, sample_objects_to_display):
    return Overlay(sample_image, sample_position, sample_objects_to_display)


def test_overlay_initialization(
    setup_pygame, sample_image, sample_position, sample_objects_to_display
):
    overlay = Overlay(sample_image, sample_position, sample_objects_to_display)
    assert overlay.image == sample_image
    assert overlay.rect.topleft == sample_position
    assert overlay.objects_to_display == sample_objects_to_display
    assert overlay.font is not None


def test_render_text_with_dict(setup_pygame, overlay):
    overlay.render_text()
    assert "time_in_seconds=100" in overlay.print_list
    assert "floattine=3.14" in overlay.print_list


def test_render_text_with_list(setup_pygame, sample_image, sample_position):
    objects_to_display = ["item1", "item2", "item3"]
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert "item1" in overlay.print_list
    assert "item2" in overlay.print_list
    assert "item3" in overlay.print_list


def test_render_text_with_string(setup_pygame, sample_image, sample_position):
    objects_to_display = "Hello, World!"
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert "Hello, World!" in overlay.print_list


def test_render_text_with_game_statistics(setup_pygame, sample_image, sample_position):
    game_stats = GameStatistics()
    game_stats.set_time_in_seconds(123)
    game_stats.set_floattime(3.14)
    overlay = Overlay(sample_image, sample_position, game_stats)
    overlay.render_text()
    assert "time_in_seconds=123" in overlay.print_list
    assert "floattime=3.14" in overlay.print_list


def test_render_text_with_landing_game_objects(
    setup_pygame, sample_image, sample_position
):
    obj1 = LandingGameObject(pygame.Surface((10, 10)), (20, 20))
    obj2 = LandingGameObject(pygame.Surface((30, 30)), (40, 40))
    obj1.pos = "(20, 20)"
    obj2.pos = "(40, 40)"
    objects_to_display = pygame.sprite.Group()
    objects_to_display.add(obj1)
    objects_to_display.add(obj2)
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    print(overlay.print_list)
    assert "pos=(20, 20)" in overlay.print_list


def test_render_text_with_unexpected_input(setup_pygame, sample_image, sample_position):
    objects_to_display = 12345  # Unexpected input type (int)
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert (
        overlay.print_list == []
    )  # Expecting an empty print_list since input type is not handled


def test_render_text_with_empty_dict(setup_pygame, sample_image, sample_position):
    objects_to_display = {}
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert (
        overlay.print_list == []
    )  # Expecting an empty print_list since the dict is empty


def test_render_text_with_empty_list(setup_pygame, sample_image, sample_position):
    objects_to_display = []
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert (
        overlay.print_list == []
    )  # Expecting an empty print_list since the list is empty


def test_render_text_with_empty_string(setup_pygame, sample_image, sample_position):
    objects_to_display = ""
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert overlay.print_list == [""]  # Expecting a single empty string in print_list


def test_render_text_with_none(setup_pygame, sample_image, sample_position):
    objects_to_display = None
    overlay = Overlay(sample_image, sample_position, objects_to_display)
    overlay.render_text()
    assert overlay.print_list == []  # Expecting an empty print_list since input is None
