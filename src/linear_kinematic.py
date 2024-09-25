from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries


class LinearKinematic:
    velocity = Vec2d()
    acceleration = Vec2d()
    mass: float = 0

    def __init__(
        self, mass: float = 0, velocity: Vec2d = Vec2d(), acceleration: Vec2d = Vec2d()
    ):
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration

    def set_velocity(self, vel: Vec2d):
        if vel > PhysicalBoundaries.MAX_SPEED:
            vel = PhysicalBoundaries.MAX_SPEED * vel.normalized()
        self.velocity = vel

    def set_acceleration(self, acc: Vec2d):
        if acc > PhysicalBoundaries.MAX_ACCELERATION:
            acc = PhysicalBoundaries.MAX_ACCELERATION * acc.normalized()
        self.acceleration = acc

    def set_mass(self, mass: float):
        if mass < 0:
            raise ValueError(f"Negative mass assigned! mass = {mass}")
        self.mass = mass
