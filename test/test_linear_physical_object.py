import pygame
import pytest

from src.colors import colors_dict
from src.linear_physical_object import LinearPhysicalObject
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d
from src.general_physics import pixel_to_meter, meter_to_pixel


@pytest.fixture
def example_image():
    img = pygame.Surface((40, 30))
    img.fill(colors_dict["red"])
    return img


class TestLinearPhysicalObject:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dimensions = Dimensions2D(4, 8)
        self.position_meter = Vec2d(10, 50)
        self.position_pixel = meter_to_pixel(Vec2d(self.position_meter))
        self.velocity = Vec2d(16, 50)
        self.acceleration = Vec2d(-10, 2)
        self.mass = 1e5

    def test_init(self, example_image):
        obj = LinearPhysicalObject(
            name="test_object",
            image=example_image,
            pos=self.position_pixel,
            mass=self.mass,
            velocity=self.velocity,
            acceleration=self.acceleration,
        )
        obj = LinearPhysicalObject(
            name="test_object",
            image=example_image,
            pos=self.position_pixel,
            mass=self.mass,
            velocity=self.velocity,
        )
        obj = LinearPhysicalObject(
            name="test_object",
            image=example_image,
            pos=self.position_pixel,
            mass=self.mass,
        )

    def test_step(self, example_image):
        time_step = 0.1
        non_admissible_time_step = -0.1

        expected_new_position_meter = (
            pixel_to_meter(self.position_pixel) + time_step * self.velocity
        )
        expected_new_velocity_meter = self.velocity + time_step * self.acceleration

        obj = LinearPhysicalObject(
            name="test_object",
            image=example_image,
            pos=self.position_pixel,
            mass=self.mass,
            velocity=self.velocity,
            acceleration=self.acceleration,
        )
        obj.step(time_step)
        assert obj.pos == meter_to_pixel(expected_new_position_meter)
        assert obj.kinematic.velocity == expected_new_velocity_meter
        with pytest.raises(ValueError):
            obj.step(non_admissible_time_step)
