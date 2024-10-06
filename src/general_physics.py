from src.common_constants import CommonConstants
from src.vec2d import Vec2d


pixel_to_meter_ratio: float = CommonConstants.PIXEL_TO_METER
meter_to_pixel_ratio: float = CommonConstants.METER_TO_PIXEL
timestep_size: float = 1 / 60


def pixel_to_meter(*args) -> float:
    if type(args[0]) == float and len(args) == 1:
        res = args[0] * pixel_to_meter_ratio
    elif type(*args) == tuple:
        res = Vec2d(*args)
    elif type(*args) == Vec2d:
        res = pixel_to_meter_ratio * args[0]
    else:
        raise TypeError(f"Only float or Vec2d acceptable, but {type(*args)} given")
    return res


def meter_to_pixel(*args) -> float:
    if type(args[0]) == float and len(args) == 1:
        res = args[0] * meter_to_pixel_ratio
    elif type(*args) == tuple:
        res = Vec2d(*args)
    elif isinstance(*args, Vec2d):
        res = meter_to_pixel_ratio * args[0]
    else:
        raise TypeError(f"Only float or Vec2d acceptable, but {type(*args)} given")
    return res
