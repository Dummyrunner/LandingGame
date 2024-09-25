import pygame
from src.linear_kinematics import LinearKinematics


class Rocket(pygame.sprite.Sprite, LinearKinematics):
    def __init__(self, x, y, width, height, color, velocity, acceleration):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = velocity
        self.acceleration = acceleration

    def move(self):
        # Interaction with global_physics
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)
