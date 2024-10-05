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


def test_overlay_initialization(overlay):
    assert overlay.image.get_alpha() == 128
    assert overlay.rect.topleft == (0, 0)
    assert overlay.font is not None
    assert overlay.line_order == []


def test_add_line(overlay):
    overlay.add_line("Test line")
    assert overlay.line_order == ["Test line"]

    overlay.add_line(123)
    assert overlay.line_order == ["Test line", "123"]

    overlay.add_line(45.67)
    assert overlay.line_order == ["Test line", "123", "45.67"]

    with pytest.raises(ValueError):
        overlay.add_line([])


def test_normalize_attributes(overlay):
    attribute_name, attribute_display_name, attribute_format_as = (
        overlay._Overlay__normalize_attributes("speed", None, None)
    )
    assert attribute_name == "speed"
    assert attribute_display_name == "speed"
    assert attribute_format_as == str

    with pytest.raises(ValueError):
        overlay._Overlay__normalize_attributes(None, None, None)

    with pytest.raises(ValueError):
        overlay._Overlay__normalize_attributes(123, None, None)


def test_format_line(overlay):
    class TestObject:
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    formatted_line = overlay._Overlay__format_line(obj, "speed", "Speed", float)
    assert formatted_line == "Speed: 123.46"

    formatted_line = overlay._Overlay__format_line(obj, "speed", "Speed", int)
    assert formatted_line == "Speed: 123"

    formatted_line = overlay._Overlay__format_line(obj, "speed", "Speed", str)
    assert formatted_line == "Speed: 123.456"


def test_get_line_from_object(overlay):
    class TestObject:
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    line = overlay._Overlay__get_line_from_object(obj, "speed", "Speed", int)
    assert line == "Speed: 123"


def test_add_attribute(overlay):
    class TestObject(LandingGameObject):
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    overlay.add_attribute(obj, "speed", "Speed", float)
    assert overlay.line_order == [(obj, "speed", "Speed", float)]


def test_get_printlist(overlay):
    overlay.add_line("Test line")
    assert overlay._Overlay__get_printlist() == ["Test line"]

    class TestObject(LandingGameObject):
        def __init__(self):
            self.speed = 123.456

    obj = TestObject()
    overlay.add_attribute(obj, "speed", "Speed", float)
    assert overlay._Overlay__get_printlist() == ["Test line", "Speed: 123.46"]


def test_attach_to_object(overlay):
    class TestObject(LandingGameObject):
        def __init__(self):
            self.rect = pygame.Rect(50, 50, 10, 10)

    obj = TestObject()
    overlay.attach_to_object(obj)
    assert overlay.attached_object == obj


def test_detach_from_object(overlay):
    class TestObject(LandingGameObject):
        def __init__(self):
            self.rect = pygame.Rect(50, 50, 10, 10)

    obj = TestObject()
    overlay.attach_to_object(obj)
    overlay.detach_from_object()
    assert overlay.attached_object is None


def test_hide_show(overlay):
    overlay.chosen_alpha = 255
    overlay.hide()
    assert overlay.image.get_alpha() == 0

    overlay.show()
    assert overlay.image.get_alpha() == 255


def test_change_font(overlay):
    new_font = pygame.font.Font(None, 24)
    overlay.change_font(new_font)
    assert overlay.font == new_font


def test_reset_overlay(overlay):
    overlay.add_line("Test line")
    overlay.reset_overlay()
    assert overlay.line_order == []


def test_remove_first_line(overlay):
    overlay.add_line("First line")
    overlay.add_line("Second line")
    overlay.remove_first_line()
    assert overlay.line_order == ["Second line"]

    overlay.remove_first_line()
    assert overlay.line_order == []

    overlay.remove_first_line()  # Should not raise an error even if the list is empty
    assert overlay.line_order == []
