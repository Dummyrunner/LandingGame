from dataclasses import dataclass
from src.landing_game_action_periodic import LandingGameActionEachFrame


def is_lambda(obj):
    return isinstance(obj, type(lambda: None)) and callable(obj)


# Keyboard access assignments in pygame https://www.pygame.org/docs/ref/key.html
@dataclass
class PygameKeyState:
    def __init__(self, key_identifier, pressed: bool):
        if not type(pressed) == bool:
            raise TypeError("pressed must be of type boolean")

        self.key_identifier = key_identifier
        self.pressed = pressed


class LandingGameActionOnKey(LandingGameActionEachFrame):
    """Defines the connection between a certain key state
    (e.g. "space bar is pressed" or "arrow key up is not pressed)
    and a callback function that will be executed under this condition"""

    def __init__(self, trigger_key_state: PygameKeyState, action_callback: callable):
        if not type(trigger_key_state) == PygameKeyState:
            raise TypeError(
                f"trigger key state must be of type PygameKeyState, but is {type(trigger_key_state)}"
            )
        super().__init__(action_callback)
        self.trigger_key = trigger_key_state
