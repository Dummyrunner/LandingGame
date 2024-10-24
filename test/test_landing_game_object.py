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
        position_pixel = Vec2d(100, 90)
        obj = LandingGameObject(image=example_image, pos=position_pixel)

        assert obj.pos == position_pixel
        assert obj.rect.width == example_image.get_width()
        assert obj.rect.height == example_image.get_height()
        assert obj.rect.center == (position_pixel.x, position_pixel.y)
