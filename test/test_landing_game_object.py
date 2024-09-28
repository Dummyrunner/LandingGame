import pygame
import pytest

from src.landing_game_object import LandingGameObject
from src.vec2d import Vec2d
from src.colors import colors_dict


@pytest.fixture
def example_image():
    img = pygame.Surface((40, 30))
    img.fill(colors_dict["red"])
    return img


class TestLandingGameObject:

    def test_initialization(self, example_image):
        position = Vec2d(100, 100)
        obj = LandingGameObject(image=example_image, pos=position)

        assert obj.pos == position
        assert obj.rect.width == example_image.get_width()
        assert obj.rect.height == example_image.get_height()
        assert obj.rect.center == (position.x, position.y)
