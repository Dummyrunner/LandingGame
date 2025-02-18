import pygame
from dataclasses import dataclass
from src.vec2d import Vec2d


@dataclass(frozen=True)
class CommonConstants:
    GRAVITATIONAL_FORCE_EARTH: float = 9.81  # m/s^2
    ROCKET_MASS = 1e5  # kg
    ROCKET_UPWARD_BOOST_FORCE_SCALAR = ROCKET_MASS * 20
    ROCKET_SIDEWAYS_BOOST_FORCE_SCALAR = ROCKET_MASS * 10
    EXHAUST_FIRE_DOWN_DIMENSIONS = Vec2d(10, 20)
    METER_TO_PIXEL: float = float(10)
    PIXEL_TO_METER: float = 1 / METER_TO_PIXEL
    FPS: int = 60
    TIME_STEP: float = 1 / FPS  # seconds
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    EGO_INITIAL_HEALTH: float = 100
    EGO_DAMAGE_SENSITIVITY: float = 5


@dataclass(frozen=True)
class PhysicalBoundaries:
    MAX_SPEED: float = 1e9
    MAX_ACCELERATION: float = 1e9


@dataclass(frozen=True)
class GameFonts:
    if not pygame.font.get_init():
        pygame.font.init()
    BASIC_FONT_TYPE: str = "Calibri"
    BASIC_FONT_SIZE: int = 16
    BASIC_FONT = pygame.font.SysFont(BASIC_FONT_TYPE, BASIC_FONT_SIZE)


@dataclass(frozen=True)
class Opacity:
    OPAQUE: int = 255
    SEMI_TRANSPARENT: int = 128
    TRANSPARENT: int = 0
