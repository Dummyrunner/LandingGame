from src.landing_game_object import LandingGameObject
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d


class TestLandingGameObject:
    def test_initialization(self):
        dimensions = Dimensions2D(200, 200)
        position = Vec2d(100, 100)
        obj = LandingGameObject(image=None, dimensions=dimensions, pos=position)

        assert obj.dimensions == dimensions
        assert obj.pos == position
        assert obj.rect.width == dimensions.width
        assert obj.rect.height == dimensions.height
        assert obj.rect.center == (position.x, position.y)

    def test_align_rect_to_position(self):
        dimensions = Dimensions2D(200, 200)
        position = Vec2d(100, 100)
        obj = LandingGameObject(image=None, dimensions=dimensions, pos=position)

        new_position = Vec2d(300, 300)
        obj.pos = new_position
        obj.align_rect_to_position()

        assert obj.rect.center == new_position
        assert obj.rect.width == dimensions.width
        assert obj.rect.height == dimensions.height
