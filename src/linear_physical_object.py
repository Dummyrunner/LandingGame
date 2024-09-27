from typing import Any
import pygame
from src.vec2d import Vec2d
from src.linear_kinematic import LinearKinematic
from src.landing_game_object import LandingGameObject


class LinearPhysicalObject(LandingGameObject, LinearKinematic):
    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):

        LandingGameObject.__init__(self, image, pos)
        self.kinematic = LinearKinematic(mass, velocity, acceleration)

    def step(self, time_step_width: float) -> None:
        """Perform timestep: update position and velocity
        from current acceleration and velocity after timestep of time_step_with (s)

        Args:
            time_step_width (float): len of timestep that should be simulated
        """
        if time_step_width < 0:
            raise ValueError(
                f"Negative time {time_step_width} handed to LinearPhysicalObject.step. Only positive time admissible!"
            )
        new_pos = self.pos + time_step_width * self.kinematic.velocity
        new_velocity = (
            self.kinematic.velocity + time_step_width * self.kinematic.acceleration
        )
        self.pos = new_pos
        self.kinematic.set_velocity(new_velocity)

    def update(self, time_step):
        self.step(time_step)
        self.rect.center = self.pos
