class IDGenerator:
    def __init__(self):
        self.id = 0

    def generate_new_id(self):
        self.id += 1
        return self.id
