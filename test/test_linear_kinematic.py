import pytest
from src.linear_kinematic import LinearKinematic
from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries

ABS_TOLERANCE = 1e-5


class TestLinearKinematic:

    def test_set_mass(self):
        obj = LinearKinematic(mass=5.0)
        assert obj.mass == 5.0
        with pytest.raises(ValueError):
            invalid_mass_value = -1
            LinearKinematic(mass=invalid_mass_value)

    def test_set_velocity(self):
        velocity_to_assign = Vec2d(111, 222)
        obj = LinearKinematic(mass=5.0, velocity=velocity_to_assign)
        assert obj.velocity == velocity_to_assign
        velocity_too_large = Vec2d(1e9, 10)
        obj_too_fast_saturate = LinearKinematic(mass=5.0, velocity=velocity_too_large)
        assert obj_too_fast_saturate.velocity.length == pytest.approx(
            PhysicalBoundaries.MAX_SPEED, ABS_TOLERANCE
        )

    def test_set_acceleration(self):
        acceleration_to_assign = Vec2d(111, 222)
        obj = LinearKinematic(mass=5.0, acceleration=acceleration_to_assign)
        assert obj.acceleration == acceleration_to_assign
        acceleration_too_large = Vec2d(1e9, 10)
        obj_too_accelerated_saturate = LinearKinematic(
            mass=5.0, velocity=Vec2d(), acceleration=acceleration_too_large
        )
        print(obj_too_accelerated_saturate.acceleration.length)
        print(PhysicalBoundaries.MAX_ACCELERATION)
        assert obj_too_accelerated_saturate.acceleration.length == pytest.approx(
            PhysicalBoundaries.MAX_SPEED, ABS_TOLERANCE
        )
