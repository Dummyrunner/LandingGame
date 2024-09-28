import pygame
from src.vec2d import Vec2d


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d = Vec2d(),
    ) -> None:
        super().__init__()
        self.rect: pygame.Rect = pygame.Surface.get_rect(image)
        self.pos = pos
        self.rect.center = self.pos
        self.image = image

    def update(self, time_step: float) -> None:
        # takes timestep argument like physical object,
        # to be able to treat them in the same way
        self.rect.center = self.pos
