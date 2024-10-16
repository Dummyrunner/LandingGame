import pygame
from src.vec2d import Vec2d
from src.linear_kinematic import LinearKinematic
from src.landing_game_object import LandingGameObject
from src.general_physics import meter_to_pixel, pixel_to_meter


class LinearPhysicalObject(LandingGameObject, LinearKinematic):
    def __init__(
        self,
        name: str,
        image: pygame.surface,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):

        LandingGameObject.__init__(self, name, image, pos)
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
        new_pos_meter = Vec2d(
            pixel_to_meter(self.pos) + time_step_width * self.kinematic.velocity
        )
        new_pos_pixel = meter_to_pixel(new_pos_meter)
        new_velocity = (
            self.kinematic.velocity + time_step_width * self.kinematic.acceleration
        )
        self.set_pos(new_pos_pixel)
        self.kinematic.set_velocity(new_velocity)

    def update(self, time_step):
        self.step(time_step)
        self.rect.center = self.pos
