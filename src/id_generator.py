from random import randint


class IDGenerator:
    def __init__(self):
        self.id = 0

    def generate_new_id(self):
        return randint(0, 1000)  # should work in most cases
