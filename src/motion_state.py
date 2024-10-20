from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries


class MotionState:
    def __init__(
        self,
        pos_meter,
        mass: float = 0,
        velocity: Vec2d = Vec2d(),
        external_forces: list = [Vec2d()],
    ):
        self.mass = mass
        self.pos_meter_precise = pos_meter
        self.velocity = velocity
        self.external_forces = external_forces

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
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"Negative mass assigned! mass = {value}")
        self._mass = value

    @property
    def external_forces(self) -> list[Vec2d]:
        if self._external_forces == []:
            self._external_forces = [Vec2d()]
        return self._external_forces

    @external_forces.setter
    def external_forces(self, forces: list[Vec2d]):
        if isinstance(forces, Vec2d):
            forces = [forces]
        elif type(forces) != list:
            raise TypeError(
                f"External forces has to be a list of Vec2d, but is {type(forces)}"
            )
        self._external_forces = forces
