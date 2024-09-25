from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries


class LinearKinematic:
    def __init__(
        self, mass: float = 0, velocity: Vec2d = Vec2d(), acceleration: Vec2d = Vec2d()
    ):
        self.mass = None
        self.velocity = None
        self.acceleration = None
        self.set_mass(mass)
        self.set_velocity(velocity)
        self.set_acceleration(acceleration)

    def set_velocity(self, vel: Vec2d):
        if vel.length > PhysicalBoundaries.MAX_SPEED:
            print("vel len: ", vel.length)
            vel = PhysicalBoundaries.MAX_SPEED * vel.normalized()
        self.velocity = vel

    def set_acceleration(self, acc: Vec2d):
        if acc.length > PhysicalBoundaries.MAX_ACCELERATION:
            acc = PhysicalBoundaries.MAX_ACCELERATION * acc.normalized()
        self.acceleration = acc

    def set_mass(self, mass: float):
        if mass < 0:
            raise ValueError(f"Negative mass assigned! mass = {mass}")
        self.mass = mass
