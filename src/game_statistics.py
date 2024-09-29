class GameStatistics:
    """Track different parameters of the running game."""

    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.time = 0
        self.floattime = 0.0

    def update(self, time: float) -> None:
        self.floattime += time
        self.time = int(self.floattime)

    def increment_score(self, increment: int) -> None:
        self.score += increment

    def decrement_lives(self) -> None:
        self.lives -= 1

    def increment_level(self) -> None:
        self.level += 1
