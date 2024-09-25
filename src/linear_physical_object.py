import pygame
from src.vec2d import Vec2d
from src.linear_kinematic import LinearKinematic
from src.landing_game_object import LandingGameObject
from src.dimensions2d import Dimensions2D


class LinearPhysicalObject(LandingGameObject, LinearKinematic):
    def __init__(
        self,
        sprite: pygame.sprite.Sprite,
        dimensions: Dimensions2D,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):

        pygame.sprite.Sprite.__init__(self)
        LandingGameObject.__init__(sprite, dimensions, pos)
        self.kinematic = LinearKinematic(mass, velocity, acceleration)

    def step(self, time_step_width: float) -> None:
        """Perform timestep: update position and velocity
        from current acceleration and velocity after timestep of time_step_with (s)

        Args:
            time_step_width (float): len of timestep that should be simulated
        """
        pos = pos + time_step_width * self.kinematic.velocity
        self.kinematic.set_velocity(
            self.kinematic.velocity + time_step_width * self.kinematic.acceleration
        )
