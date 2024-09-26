from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d
from src.linear_physical_object import LinearPhysicalObject


class Rocket(LinearPhysicalObject):
    def __init__(
        self,
        dimensions: Dimensions2D,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):
        LinearPhysicalObject.__init__(dimensions, pos, mass, velocity, acceleration)
