class GameTiming:
    """Track different parameters of the running game."""

    def __init__(self):
        self.time = 0

    def update(self, time: float) -> None:
        self.time += time
