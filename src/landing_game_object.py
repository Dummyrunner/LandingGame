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
        pos: Vec2d = Vec2d(),
    ) -> None:
        """LandingGameObject constructor.

        Args:
            image (pygame.surface): pygame.surface that defines the object's visual representation
            pos (Vec2d, optional): 2d Position in pixel. (0,0) represents left top corner. Defaults to Vec2d().
        """
        super().__init__()
        self.ID = self.ID_generator.assign_ID()
        self.rect: pygame.Rect = pygame.Surface.get_rect(image)
        self.rect.center = Vec2d(pos)
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
