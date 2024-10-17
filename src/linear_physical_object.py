import pygame
from src.vec2d import Vec2d
from src.motion_state import MotionState
from src.landing_game_object import LandingGameObject
from src.general_physics import meter_to_pixel, pixel_to_meter


def round_vec2d_meter_to_pixel(floatvec: Vec2d) -> Vec2d:
    x = meter_to_pixel(floatvec[0])
    y = meter_to_pixel(floatvec[1])
    return Vec2d(round(x), round(y))


class LinearPhysicalObject(LandingGameObject, MotionState):
    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        external_forces: list = [Vec2d()],
    ):
        LandingGameObject.__init__(self, image, pos)
        self.kinematic = MotionState(
            pixel_to_meter(pos), mass, velocity, external_forces
        )

    def step(self, time_step_width: float) -> None:
        """Perform timestep: update position and velocity
        from current acceleration and velocity after timestep of time_step_with (s)

        Args:
            time_step_width (float): len of timestep that should be simulated
        """
        if self.kinematic.external_forces == []:
            self.kinematic.external_forces = [Vec2d()]
        resulting_external_force = sum(self.kinematic.external_forces)
        acceleration = +(1 / self.kinematic.mass) * resulting_external_force

        if time_step_width < 0:
            raise ValueError(
                f"Negative time {time_step_width} handed to LinearPhysicalObject.step. Only positive time admissible!"
            )
        new_pos_meter = Vec2d(
            self.kinematic.pos_meter_precise + time_step_width * self.kinematic.velocity
        )
        self.kinematic.pos_meter_precise = new_pos_meter
        new_velocity = self.kinematic.velocity + time_step_width * acceleration
        self.kinematic.velocity = new_velocity

        self.pos = meter_to_pixel(new_pos_meter)

        self.kinematic.external_forces = [Vec2d()]

    def update(self, time_step):
        self.step(time_step)
        self.rect.center = round_vec2d_meter_to_pixel(self.kinematic.pos_meter_precise)
