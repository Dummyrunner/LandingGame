import pygame
from src.vec2d import Vec2d


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d = Vec2d(),
    ) -> None:
        self.rect: pygame.Rect = pygame.Surface.get_rect(image)
        self.pos = pos
        self.image = image
