import pytest
import pygame
from src.overlay import Overlay
from src.landing_game_object import LandingGameObject


@pytest.fixture
def overlay():
    pygame.init()
    image = pygame.Surface((200, 100))
    font = pygame.font.Font(None, 36)
    return Overlay(image, font)


def test_add_line(overlay):
    overlay.add_line("Test line")
    assert "Test line" in overlay.line_order

    overlay.add_line(123)
    assert "123" in overlay.line_order

    overlay.add_line(45.67)
    assert "45.67" in overlay.line_order

    with pytest.raises(ValueError):
        overlay.add_line([])


def test_normalize_attributes(overlay):
    attribute_name, attribute_display_name, attribute_format_as = (
        overlay.normalize_attributes("speed", None, None)
    )
    assert attribute_name == "speed"
    assert attribute_display_name == "speed"
    assert attribute_format_as == str

    with pytest.raises(ValueError):
        overlay.normalize_attributes(None, None, None)

    with pytest.raises(ValueError):
        overlay.normalize_attributes(123, None, None)


def test_format_line(overlay):
    class TestObject:
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    line = overlay.format_line(obj, "speed", "Speed", float)
    assert line == "Speed: 123.46"

    line = overlay.format_line(obj, "speed", "Speed", int)
    assert line == "Speed: 123"

    line = overlay.format_line(obj, "speed", "Speed", str)
    assert line == "Speed: 123.456"


def test_get_line_from_object(overlay):
    class TestObject:
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    overlay.get_line_from_object(obj, "speed", "Speed", float)
    assert "Speed: 123.46" in overlay.line_order


def test_add_attribute(overlay):
    class TestObject(LandingGameObject):
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    overlay.add_attribute(obj, "speed", "Speed", float)
    assert (obj, "speed", "Speed", float) in overlay.line_order


def test_get_printlist(overlay):
    overlay.add_line("Test line")
    print_list = overlay.get_printlist()
    assert "Test line" in overlay.print_list


def test_render_text(overlay):
    overlay.render_text(["Test line"])
    assert overlay.image.get_at((0, 0)) == pygame.Color(255, 255, 255, 255)


def test_update(overlay):
    overlay.add_line("Test line")
    overlay.update(0)
    assert overlay.image.get_at((0, 0)) == pygame.Color(255, 255, 255, 255)
