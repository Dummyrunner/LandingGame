import pygame
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


@dataclass(frozen=True)
class GameColors:
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    RED: tuple = (255, 0, 0)
    GREEN: tuple = (0, 255, 0)
    BLUE: tuple = (0, 0, 255)


@dataclass(frozen=True)
class GameFonts:
    if not pygame.font.get_init():
        pygame.font.init()
    BASIC_FONT_TYPE: str = "Calibri"
    BASIC_FONT_SIZE: int = 16
    BASIC_FONT = pygame.font.SysFont(BASIC_FONT_TYPE, BASIC_FONT_SIZE)
