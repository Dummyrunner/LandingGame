import pygame
from src.dimensions2d import Dimensions2D
from src.vec2d import Vec2d


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    def __init__(
        self,
        image: pygame.surface,
        dimensions: Dimensions2D = Dimensions2D(),
        pos: Vec2d = Vec2d(),
    ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.pos = pos
        self.dimensions = dimensions
        self.image = image
        self.align_rect_to_position()

    def align_rect_to_position(self) -> None:
        """Assign current position and dimensions to object's rect"""
        self.rect.width = self.dimensions.width
        self.rect.height = self.dimensions.height
        self.rect.center = (self.pos.x, self.pos.y)
