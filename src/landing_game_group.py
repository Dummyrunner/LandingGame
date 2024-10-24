import pygame


class LandingGameGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.__name_to_object_dict = {}

    def name_object(self, name: str, obj):
        if obj not in self:
            raise ValueError("Object not in group")
        if name in self.__name_to_object_dict:
            raise ValueError("Name already in use")
        self.__name_to_object_dict[name] = obj

    def get_object_by_name(self, name: str):
        return self.__name_to_object_dict[name]

    def remove_object_by_name(self, name: str):
        del self.__name_to_object_dict[name]

    def get_object_by_id(self, id: int):
        for obj in self:
            if obj.id == id:
                return obj
        raise ValueError("Object not found")

    def remove_object_by_id(self, id: int):
        obj = self.get_object_by_id(id)
        self.remove(obj)

    def remove(self, sprite):
        super().remove(sprite)
        keys_to_delete = [
            name for name, obj in self.__name_to_object_dict.items() if obj == sprite
        ]
        for key in keys_to_delete:
            del self.__name_to_object_dict[key]
