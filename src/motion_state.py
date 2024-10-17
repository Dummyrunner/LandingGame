from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries


class MotionState:
    def __init__(
        self,
        pos_meter,
        mass: float = 0,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):
        if mass < 0:
            raise ValueError(f"Negative mass assigned! mass = {mass}")
        self._mass = mass
        self._pos_meter_precise = pos_meter
        self._velocity = velocity
        self._acceleration = acceleration

    @property
    def pos_meter_precise(self) -> Vec2d:
        return self._pos_meter_precise

    @pos_meter_precise.setter
    def pos_meter_precise(self, pos_meter: Vec2d):
        self._pos_meter_precise = pos_meter

    @property
    def velocity(self) -> Vec2d:
        return self._velocity

    @velocity.setter
    def velocity(self, vel: Vec2d):
        if vel.length > PhysicalBoundaries.MAX_SPEED:
            vel = PhysicalBoundaries.MAX_SPEED * vel.normalized()
        self._velocity = vel

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value: Vec2d) -> None:
        if value.length > PhysicalBoundaries.MAX_ACCELERATION:
            normalized_value = value.normalized()
            self._acceleration = PhysicalBoundaries.MAX_ACCELERATION * normalized_value
        else:
            self._acceleration = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Negative mass assigned! mass = {value}")
        self._mass = value
