import pygame

from src.common_constants import Opacity
from src.vec2d import Vec2d


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    def __init__(
        self,
        image: pygame.surface,
        pos_pixel: Vec2d = Vec2d(),
    ) -> None:
        super().__init__()
        self.rect: pygame.Rect = pygame.Surface.get_rect(image)
        self.rect.center = Vec2d(pos_pixel)
        self.add_pos_to_dict()
        self.image = image

    def update(self, *args) -> None:
        pass

    def set_color(self, color, alpha=Opacity.OPAQUE):
        self.image.fill(color)
        self.image.set_alpha(alpha)

    @property
    def pos(self) -> Vec2d:
        return Vec2d(self.rect.center)

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def set_pos(self, pos_pixel: Vec2d) -> None:
        """set position in pixel standard coordinate system

        Args:
            pos_pixel (Vec2d): position in pixels
        """
        self.rect.center = Vec2d(pos_pixel)
        self.add_pos_to_dict()

    def add_pos_to_dict(self):
        self.__dict__.update({"pos": self.pos})
