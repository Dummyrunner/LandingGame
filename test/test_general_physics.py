import pytest
from src.general_physics import meter_to_pixel, pixel_to_meter, timestep_size
from src.common_constants import CommonConstants
from src.vec2d import Vec2d


def test_time_step_size_defined():
    assert timestep_size


def test_pixel_meter_conversion_scalar():
    test_meter_distance = 3.5
    test_pixel_distance = test_meter_distance * CommonConstants.METER_TO_PIXEL
    assert meter_to_pixel(test_meter_distance) == test_pixel_distance
    assert pixel_to_meter(test_pixel_distance) == test_meter_distance


def test_pixel_meter_conversion_vec2d():
    test_meter_vec = Vec2d(1.2, 3.5)
    test_pixel_vec = CommonConstants.METER_TO_PIXEL * test_meter_vec
    assert meter_to_pixel(test_meter_vec).x == pytest.approx(test_pixel_vec.x)
    assert meter_to_pixel(test_meter_vec).y == pytest.approx(test_pixel_vec.y)
    assert pixel_to_meter(test_pixel_vec).x == pytest.approx(test_meter_vec.x)
    assert pixel_to_meter(test_pixel_vec).y == pytest.approx(test_meter_vec.y)


def test_pixel_meter_conversion_invalid_type():
    invalid_input = "non-float-and-non-vec-value"
    with pytest.raises(TypeError):
        meter_to_pixel(invalid_input)
    with pytest.raises(TypeError):
        pixel_to_meter(invalid_input)
