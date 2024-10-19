import pytest
from src.motion_state import MotionState
from src.vec2d import Vec2d
from src.common_constants import PhysicalBoundaries

ABS_TOLERANCE = 1e-5
example_pos_meter_vector = Vec2d(1.2, 2.3)


class TestMotionState:

    def test_set_mass(self):
        obj = MotionState(pos_meter=example_pos_meter_vector, mass=5.0)
        assert obj.mass == 5.0
        with pytest.raises(ValueError):
            invalid_mass_value = -1
            MotionState(pos_meter=example_pos_meter_vector, mass=invalid_mass_value)

    def test_set_velocity(self):
        velocity_to_assign = Vec2d(111, 222)
        obj = MotionState(
            pos_meter=example_pos_meter_vector, mass=5.0, velocity=velocity_to_assign
        )
        assert obj.velocity == velocity_to_assign
        velocity_too_large = Vec2d(PhysicalBoundaries.MAX_SPEED + 1, 10)
        obj_too_fast_saturate = MotionState(
            pos_meter=example_pos_meter_vector, mass=5.0, velocity=velocity_too_large
        )
        assert obj_too_fast_saturate.velocity.length == pytest.approx(
            PhysicalBoundaries.MAX_SPEED, ABS_TOLERANCE
        )

    def test_set_external_forces(self):
        external_forces_to_assign = [Vec2d(111, 222)]
        obj = MotionState(
            pos_meter=example_pos_meter_vector,
            mass=5.0,
            external_forces=external_forces_to_assign,
        )
        with pytest.raises(TypeError):
            non_vector_object = 123
            obj.external_forces = non_vector_object
        assert obj.external_forces == external_forces_to_assign

    def test_set_external_forces_single_vector(self):
        external_forces_to_assign_vector = Vec2d(111, 222)
        obj = MotionState(
            pos_meter=example_pos_meter_vector,
            mass=5.0,
            external_forces=external_forces_to_assign_vector,
        )
        assert type(obj.external_forces) == list
        assert obj.external_forces == [external_forces_to_assign_vector]
