from src.common_constants import CommonConstants


class GlobalPhysics:
    def __init__(self):
        self.gravity = CommonConstants.GRAVITATION
        self.air_density = CommonConstants.AIR_DENSITY
        self.physical_objects = []

    def step_physics(self):
        pass

    def collision_detection(self):
        pass
