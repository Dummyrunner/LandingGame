import pygame


class ObjectLibrary:
    """
    This class is responsible for generating unique IDs for objects.
    """

    def __init__(self):
        self.game_objects = {}
        self.next_ID = 0
        self.used_IDs = []

    def add_game_object(self, game_object):
        """Adds a game object to the library."""
        if game_object.name in self.game_objects:
            raise ValueError("Object with this name already exists.")
        self.game_objects[game_object.name] = game_object

    def get_ID(self):
        """Returns a unique ID for an object."""
        self.next_ID += 1
        self.used_IDs.append(self.next_ID)
        return self.next_ID

    def get_used_IDs(self):
        """Returns all IDs that have been used so far."""
        return self.used_IDs

    def update(self, time_step):
        for obj in self.game_objects.values():
            obj.update(time_step)

    def blit(self, display):
        for obj in self.game_objects.values():
            display.blit(obj.image, obj.rect)
