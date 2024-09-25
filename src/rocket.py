import pygame
from src.dimensions2d import Dimensions2D
from src.linear_kinematics import LinearKinematic
from src.vec2d import Vec2d
from src.landing_game_object import LandingGameObject
from src.linear_physical_object import LinearPhysicalObject


class Rocket(LinearPhysicalObject):
    def __init__(
        self,
        sprite: pygame.sprite.Sprite,
        dimensions: Dimensions2D,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        acceleration: Vec2d = Vec2d(),
    ):
        LinearPhysicalObject.__init__(
            sprite, dimensions, pos, mass, velocity, acceleration
        )
