class IDGenerator:
    def __init__(self):
        self.current_id = 0

    def assign_ID(self):
        self.current_id += 1
        return self.current_id
