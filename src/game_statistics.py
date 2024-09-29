class GameStatistics:
    """Track different parameters of the running game."""

    def __init__(self):
        self.time_in_seconds = 0
        self.floattime = 0.0

    def update(self, time: float) -> None:
        self.floattime += time
        self.time_in_seconds = int(self.floattime)

    def increment_score(self, increment: int) -> None:
        self.score += increment

    def decrement_lives(self) -> None:
        self.lives -= 1

    def increment_level(self) -> None:
        self.level += 1
