import pytest
from src.general_physics import meter_to_pixel, pixel_to_meter, timestep_size
from src.common_constants import CommonConstants
from src.vec2d import Vec2d


test_vector = Vec2d(1.2, 3.5)
test_tuple = (1.2, 3.5)
test_scalar_float = 3.5
test_scalar_int = 3


def test_time_step_size_defined():
    assert timestep_size


test_data_scalar = [
    (
        test_scalar_float,
        test_scalar_float * CommonConstants.METER_TO_PIXEL,
        test_scalar_float * CommonConstants.PIXEL_TO_METER,
    ),
    (
        test_scalar_int,
        test_scalar_int * CommonConstants.METER_TO_PIXEL,
        test_scalar_int * CommonConstants.PIXEL_TO_METER,
    ),
]

test_data_2dim = [
    (
        test_vector,
        test_vector * CommonConstants.METER_TO_PIXEL,
        test_vector * CommonConstants.PIXEL_TO_METER,
    ),
    (
        test_tuple,
        (
            test_tuple[0] * CommonConstants.METER_TO_PIXEL,
            test_tuple[1] * CommonConstants.METER_TO_PIXEL,
        ),
        (
            test_tuple[0] * CommonConstants.PIXEL_TO_METER,
            test_tuple[1] * CommonConstants.PIXEL_TO_METER,
        ),
    ),
]


@pytest.mark.parametrize(
    "input_scalar,expected_pixel_scalar,expected_meter_scalar", test_data_scalar
)
def test_pixel_meter_conversion_scalar(
    input_scalar, expected_pixel_scalar, expected_meter_scalar
):
    output_pixel = meter_to_pixel(input_scalar)
    output_meter = pixel_to_meter(input_scalar)

    assert output_pixel == pytest.approx(expected_pixel_scalar)
    assert output_meter == pytest.approx(expected_meter_scalar)


@pytest.mark.parametrize(
    "input_2d, expected_pixel_2d, expected_meter_2d", test_data_2dim
)
def test_pixel_meter_conversion_2dim(input_2d, expected_pixel_2d, expected_meter_2d):

    output_pixel = meter_to_pixel(input_2d)
    output_meter = pixel_to_meter(input_2d)
    assert output_pixel[0] == pytest.approx(expected_pixel_2d[0])
    assert output_pixel[1] == pytest.approx(expected_pixel_2d[1])
    assert output_meter[0] == pytest.approx(expected_meter_2d[0])
    assert output_meter[1] == pytest.approx(expected_meter_2d[1])


def test_pixel_meter_conversion_invalid_type():
    invalid_input = "non-float-and-non-vec-value"
    with pytest.raises(TypeError):
        meter_to_pixel(invalid_input)
    with pytest.raises(TypeError):
        pixel_to_meter(invalid_input)
