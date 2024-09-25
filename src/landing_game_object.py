import pygame
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    def __init__(
        self,
        sprite: pygame.sprite.Sprite = None,
        dimensions: Dimensions2D = Dimensions2D(),
        pos: Vec2d = Vec2d(),
    ) -> None:
        self.rect: pygame.Rect = None
        self.sprite = sprite
        self.pos = pos
        self.dimensions = dimensions
        self.align_rect_to_position()

    def align_rect_to_position(self) -> None:
        """Assign current position and dimensions to object's rect"""
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.rect.width = self.dimensions.width
        self.rect.height = self.dimensions.height
