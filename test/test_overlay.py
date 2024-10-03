import pytest
import pygame
from src.overlay import Overlay


@pytest.fixture
def overlay():
    pygame.init()
    image = pygame.Surface((200, 100))
    font = pygame.font.Font(None, 36)
    alpha = 128
    position = (10, 10)
    return Overlay(image, font, alpha, position)


def test_overlay_initialization(overlay):
    assert overlay.image.get_alpha() == 128
    assert overlay.rect.topleft == (10, 10)
    assert overlay.font is not None
    assert overlay.print_list == []


def test_add_line(overlay):
    overlay.add_line("Test line")
    assert overlay.print_list == ["Test line"]
    overlay.add_line(123)
    assert overlay.print_list == ["Test line", "123"]
    overlay.add_line(45.67)
    assert overlay.print_list == ["Test line", "123", "45.67"]
    with pytest.raises(ValueError):
        overlay.add_line([1, 2, 3])


def test_normalize_attributes():
    overlay = Overlay(
        pygame.Surface((200, 100)), pygame.font.Font(None, 36), 128, (10, 10)
    )
    attribute_name, attribute_display_name, attribute_format_as = (
        overlay.normalize_attributes("speed", None, None)
    )
    assert attribute_name == "speed"
    assert attribute_display_name == "speed"
    assert attribute_format_as == str

    with pytest.raises(ValueError):
        overlay.normalize_attributes(None, "Speed", float)


def test_format_line():
    class DummyObject:
        def __init__(self):
            self.speed = 123.456
            self.name = "TestObject"
            self.count = 42

    obj = DummyObject()
    overlay = Overlay(
        pygame.Surface((200, 100)), pygame.font.Font(None, 36), 128, (10, 10)
    )

    formatted_line = overlay.format_line(obj, "speed", "Speed", float)
    assert formatted_line == "Speed: 123.46"

    formatted_line = overlay.format_line(obj, "name", "Name", str)
    assert formatted_line == "Name: TestObject"

    formatted_line = overlay.format_line(obj, "count", "Count", int)
    assert formatted_line == "Count: 42"


def test_add_attribute():
    class DummyObject:
        def __init__(self):
            self.speed = 123.456

    obj = DummyObject()
    overlay = Overlay(
        pygame.Surface((200, 100)), pygame.font.Font(None, 36), 128, (10, 10)
    )

    overlay.read_attributes(obj, "speed", "Speed", float)
    assert overlay.print_list == ["Speed: 123.46"]


def test_render_text(overlay):
    overlay.print_list = ["Hello", "World"]
    overlay.render_text(overlay.print_list)
    assert overlay.image.get_at((0, 0)) != (0, 0, 0, 0)  # Check that text is rendered


def test_update(overlay):
    overlay.print_list = ["Update", "Test"]
    overlay.update(0)
    assert overlay.image.get_at((0, 0)) != (0, 0, 0, 0)  # Check that text is rendered


if __name__ == "__main__":
    pytest.main()
