import pygame
from src.vec2d import Vec2d
from src.linear_physical_object import LinearPhysicalObject
from src.common_constants import CommonConstants


class Rocket(LinearPhysicalObject):
    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        external_forces: Vec2d = [Vec2d()],
    ):
        LinearPhysicalObject.__init__(self, image, pos, mass, velocity, external_forces)
        self.fuel = CommonConstants.FUEL_INITIAL_AMOUNT

    def step(self, time_step_width: float) -> None:
        """Perform timestep: update position and velocity
        from current acceleration and velocity after timestep of time_step_with (s)

        Args:
            time_step_width (float): len of timestep that should be simulated
        """
        super().step(time_step_width)

    def activate_engine(self, force_vector: Vec2d) -> None:
        if self.fuel > 0:
            self.kinematic.external_forces.append(force_vector)
            self.__decrease_fuel(
                force_vector.norm() * CommonConstants.FUEL_CONSUMPTION_RATE
            )
        else:
            print("ENGINE NOT USABLE, FUEL EMPTY !!!")

    def __decrease_fuel(self, amount: float) -> None:
        self.fuel = max(0, self.fuel - amount)
