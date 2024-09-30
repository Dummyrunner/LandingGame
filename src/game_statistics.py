class GameStatistics:
    """Track different parameters of the running game."""

    def __init__(self):
        self.time_in_seconds = 0
        self.floattime = 0.0

    def update(self, time: float) -> None:
        self.floattime += time
        self.time_in_seconds = int(self.floattime)

    def set_time_in_seconds(self, time: int) -> None:
        self.time_in_seconds = time
        self.floattime = float(time)

    def set_floattime(self, time: float) -> None:
        self.floattime = time
        self.time_in_seconds = int(time)

    def get_time_in_seconds(self) -> int:
        return self.time_in_seconds

    def get_floattime(self) -> float:
        return self.floattime
