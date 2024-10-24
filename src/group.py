import pygame


class Group(pygame.sprite.Group):
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

    def remove(self, sprite):
        super().remove(sprite)
        for name, obj in self.__name_to_object_dict.items():
            if obj == sprite:
                del self.__name_to_object_dict[name]
