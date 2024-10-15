class ObjectLibrary:
    """
    This class is responsible for generating unique IDs for objects.
    """

    def __init__(self):
        self.next_ID = 0
        self.used_IDs = []

    def get_ID(self):
        """Returns a unique ID for an object."""
        self.next_ID += 1
        self.used_IDs.append(self.next_ID)
        return self.next_ID

    def get_used_IDs(self):
        """Returns all IDs that have been used so far."""
        return self.used_IDs
