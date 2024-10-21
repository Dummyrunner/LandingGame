import pygame


class IDSCOPE:
    def __init__(self, object_list=[]):
        self.object_list = object_list
        self.name_to_id = self.create_standard_ids()

    def create_standard_ids(self):
        return {
            "ego": 0,
            "ground": 1,
            "platform": 2,
        }

    def name_object(self, obj, name):
        if name in self.name_to_id:
            raise ValueError(f"Name {name} already in use!")
        if obj.id in self.name_to_id.values():
            raise ValueError(f"Object already has a name!")
        self.name_to_id[name] = obj.id

    def get_id(self, name: str = None):
        if name is None:
            max_id = 3
            for objekt in self.object_list:
                if objekt.id > max_id:
                    max_id = objekt.id
            return max_id + 1
        return self.name_to_id[name]
