import pygame
import pytest

from src.colors import colors_dict
from src.linear_physical_object import LinearPhysicalObject
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d


@pytest.fixture
def example_image():
    img = pygame.Surface((40, 30))
    img.fill(colors_dict["red"])
    return img


class TestLinearPhysicalObject:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dimensions = Dimensions2D(4, 8)
        self.position = Vec2d(10, 50)
        self.velocity = Vec2d(5, 50)
        self.acceleration = Vec2d(-10, 2)
        self.mass = 1e5

    def test_init(self, example_image):
        obj = LinearPhysicalObject(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
            acceleration=self.acceleration,
        )
        obj = LinearPhysicalObject(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
        )
        obj = LinearPhysicalObject(
            image=example_image,
            pos=self.position,
            mass=self.mass,
        )

    def test_step(self, example_image):
        time_step = 0.1
        non_admissible_time_step = -0.1

        expected_new_velocity = self.velocity + time_step * self.acceleration
        expected_new_position = self.position + time_step * self.velocity

        obj = LinearPhysicalObject(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
            acceleration=self.acceleration,
        )
        obj.step(time_step)
        assert obj.pos == expected_new_position
        assert obj.kinematic.velocity == expected_new_velocity
        with pytest.raises(ValueError):
            obj.step(non_admissible_time_step)
