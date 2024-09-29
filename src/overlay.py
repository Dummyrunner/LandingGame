import pygame
from src.landing_game_object import LandingGameObject


class Overlay(LandingGameObject):
    def __init__(self, image, position=(0, 0), obj_list: LandingGameObject = []):
        super().__init__(image, position)
        fontsize = 16
        self.image.set_alpha(128)
        self.font = pygame.font.SysFont("calibri", fontsize)
        self.obj_list = obj_list
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def render_text(self, fontsize=16):
        self.image.fill((0, 0, 0))
        line = 0
        for i, obj in enumerate(self.obj_list):
            if obj is not self:
                for attribute in vars(obj):
                    text_surface = self.font.render(
                        f"{attribute}={getattr(obj, attribute)}",
                        True,
                        (255, 255, 255),
                    )
                    self.image.blit(text_surface, (0, line * fontsize))
                    line += 1
                line += 1

    def update(self, time_step):
        self.render_text()
