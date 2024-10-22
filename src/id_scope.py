import pygame

from src.landing_game_object import LandingGameObject


class IDSCOPE:
    def __init__(self, object_list: pygame.sprite.Group):
        self.object_list = object_list
        self.standard_ids = {}
        self.name_to_id = {}

    def set_standard_ids(self, standard_ids: dict):
        """Set the standard ids for the game"""
        if len(self.standard_ids) > 0:
            raise ValueError("Standard ids already set!")
        self.standard_ids = standard_ids

    def name_object(self, obj: LandingGameObject, name: str):
        """Name an object by storing a name and the objects id in the name_to_id dictionary"""
        if name in self.name_to_id:
            raise ValueError(f"Name {name} already in use!")
        if obj.id in self.name_to_id.values():
            raise ValueError(f"Object already has a name!")
        self.name_to_id[name] = obj.id

    def create_id(self, name: str = None):
        """Create a new id for an object or return"""
        if name is None:
            unavailable_ids = [o.id for o in self.object_list]
            unavailable_ids += list(self.standard_ids.values())
            new_id = max(unavailable_ids) + 1
            return new_id

        if name not in self.standard_ids:
            raise KeyError(f"Name {name} not found in name_to_id dictionary!")

        return self.standard_ids[name]

    def add_object(self, obj: LandingGameObject):
        if obj.id in [o.id for o in self.object_list]:
            raise ValueError(f"Object with id {obj.id} already in object list!")
        self.object_list.add(obj)
