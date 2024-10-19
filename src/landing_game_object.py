import pygame

from src.common_constants import Opacity
from src.vec2d import Vec2d
from src.id_generator import IDGenerator


class LandingGameObject(pygame.sprite.Sprite):
    """Object that takes sprite representation, dimensions, position and stores according rect"""

    ID_generator = IDGenerator()

    def __init__(
        self,
        image: pygame.surface,
        pos_pixel: Vec2d = Vec2d(),
    ) -> None:
        super().__init__()
        self.ID = self.ID_generator.assign_ID()
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

    def set_pos(self, pos_pixel: Vec2d) -> None:
        """set position in pixel standard coordinate system

        Args:
            pos_pixel (Vec2d): position in pixels
        """
        self.rect.center = Vec2d(pos_pixel)
        self.add_pos_to_dict()

    def add_pos_to_dict(self):
        self.__dict__.update({"pos": self.pos})

    def __del__(self):
        self.ID_generator.used_ids.remove(self.ID)
        del self
