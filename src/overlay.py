import pygame
from src.landing_game_object import LandingGameObject


class Overlay(LandingGameObject):
    def __init__(self, image, position=(0, 0), obj_list: LandingGameObject = []):
        super().__init__(image, position)
        fontsize = 24
        self.image.set_alpha(128)
        self.font = pygame.font.Font(pygame.font.get_default_font(), fontsize)
        self.obj_list = obj_list
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def render_text(self, fontsize=24):
        for i, obj in enumerate(self.obj_list):
            if obj is not self:
                text_surface = self.font.render(
                    f"Obj {i}: Vars={vars(obj).values()}",
                    True,
                    (255, 255, 255),
                )
                self.image.blit(text_surface, (0, i * fontsize))

    def update(self, time_step):
        self.render_text()
