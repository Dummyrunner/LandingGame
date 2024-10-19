class IDGenerator:
    def __init__(self):
        self.current_id = 0
        self.used_ids = []

    def assign_ID(self):
        self.current_id += 1
        self.used_ids.append(self.current_id)
        return self.current_id

    def assign_rocket_ID(self):
        if 0 in self.used_ids:
            raise ValueError("Only one rocket object is allowed")
        else:
            self.used_ids.append(0)
            return 0
