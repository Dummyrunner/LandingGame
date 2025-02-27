import pygame
import pytest

from src.colors import colors_dict
from src.rocket import Rocket
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d
from src.general_physics import pixel_to_meter, meter_to_pixel
from src.common_constants import CommonConstants


@pytest.fixture
def example_image():
    img = pygame.Surface((40, 30))
    img.fill(colors_dict["red"])
    return img


class TestRocket:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dimensions = Dimensions2D(4, 8)
        self.position = Vec2d(10, 50)
        self.velocity = Vec2d(5, 50)
        self.acceleration = Vec2d(-10, 2)
        self.external_forces = [self.acceleration * CommonConstants.ROCKET_MASS]
        self.mass = 1e5

    def test_init(self, example_image):
        Rocket(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
            external_forces=self.external_forces,
        )
        Rocket(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
        )
        Rocket(
            image=example_image,
            pos=self.position,
            mass=self.mass,
        )

    def test_step(self, example_image):
        # Given
        time_step = 0.1
        non_admissible_time_step = -0.1

        expected_new_position_meter = (
            pixel_to_meter(self.position) + time_step * self.velocity
        )
        expected_new_velocity_meter = self.velocity + time_step * self.acceleration

        # When
        obj = Rocket(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
            external_forces=self.external_forces,
        )
        obj.kinematic.external_forces = [obj.kinematic.mass * self.acceleration]
        obj.step(time_step)

        # Then
        assert obj.pos == meter_to_pixel(expected_new_position_meter)
        assert obj.kinematic.velocity == expected_new_velocity_meter
        with pytest.raises(ValueError):
            obj.step(non_admissible_time_step)

    def test_activate_engine(self, example_image):
        # Given
        force_vector = Vec2d(0, -1)
        initial_fuel = 100
        fuel_consumption_rate = CommonConstants.FUEL_CONSUMPTION_RATE
        expected_fuel = max(
            0, initial_fuel - fuel_consumption_rate * force_vector.norm()
        )

        # When
        obj = Rocket(
            image=example_image,
            pos=self.position,
            mass=self.mass,
            velocity=self.velocity,
            external_forces=[],
        )
        obj.fuel = initial_fuel
        obj.activate_engine(force_vector)

        # Then
        assert sum(obj.kinematic.external_forces) == force_vector
        assert obj.fuel == expected_fuel
        obj.activate_engine(force_vector)
