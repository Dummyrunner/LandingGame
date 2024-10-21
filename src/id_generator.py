class IDGenerator:
    def __init__(self):
        self.current_id = 0
        self.used_ids = []

    def generate_id(self):
        self.current_id += 1
        while self.current_id in self.used_ids:
            self.current_id += 1
        self.used_ids.append(self.current_id)
        return self.current_id

    def assign_rocket_ID(self):
        if 0 in self.used_ids:
            raise ValueError("Only one rocket object is allowed")
        else:
            self.used_ids.append(0)
            return 0

    def remove_id(self, id):
        self.used_ids.remove(id)
