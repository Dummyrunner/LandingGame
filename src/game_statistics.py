class GameStatistics:
    """Track different parameters of the running game."""

    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.time = 0

    def update(self, score: int, lives: int, level: int, time: float) -> None:
        self.score = score
        self.lives = lives
        self.level = level
        self.time = time
