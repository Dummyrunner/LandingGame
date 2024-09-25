from dataclasses import dataclass


@dataclass(frozen=True)
class CommonConstants:
    GRAVITATION: float = 9.81  # m/s^2
    AIR_DENSITY: float = 1.225  # kg/m^3 at sea level
    DRAG_COEFFICIENT: float = 0.47  # for a sphere
    TIME_STEP: float = 0.01  # seconds
    PIXEL_TO_METER: float = 1 / 100
    METER_TO_PIXEL: float = 100
    FPS: int = 60
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600


@dataclass(frozen=True)
class PhysicalBoundaries:
    MAX_SPEED: float = 1e9
    MAX_ACCELERATION: float = 1e9
