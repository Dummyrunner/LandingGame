import pygame
from src.vec2d import Vec2d
from src.linear_physical_object import LinearPhysicalObject
from src.common_constants import CommonConstants


class Rocket(LinearPhysicalObject):
    def __init__(
        self,
        image: pygame.surface,
        pos: Vec2d,
        mass: float,
        velocity: Vec2d = Vec2d(),
        external_forces: Vec2d = [Vec2d()],
    ):
        LinearPhysicalObject.__init__(self, image, pos, mass, velocity, external_forces)
        self.health: int = CommonConstants.EGO_INITIAL_HEALTH

    def apply_vertical_collision_damage(self, challenger) -> None:
        """given ego and challenger collide vertically,
        apply damage to ego based on vertical velocity difference

        Args:
            ego (): Object that has a velocity and health
            challenger (LinearPhysicalObject): Object that has a velocity
        """
        ego_vertical_v = self.kinematic.velocity.y
        challenger_vertical_v = challenger.kinematic.velocity.y
        vertical_crash_velocity = abs(ego_vertical_v - challenger_vertical_v)
        damage = vertical_crash_velocity * CommonConstants.EGO_DAMAGE_SENSITIVITY
        self.__damage_object(damage)

    def __damage_object(self, damage: float) -> None:
        self.health = max(self.health - damage, 0)
