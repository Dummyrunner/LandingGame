from src.common_constants import CommonConstants


class Environment:
    def __init__(self) -> None:
        self.pixel_to_meter_ratio = CommonConstants.PIXEL_TO_METER
        self.meter_to_pixel_ratio = CommonConstants.METER_TO_PIXEL
        self.timestep_size = 1 / 60

    def pixel_to_meter(self, pixel: float) -> float:
        return pixel * self.pixel2meter

    def meter_to_pixel(self, meter: float) -> float:
        return meter * self.meter2pixel
