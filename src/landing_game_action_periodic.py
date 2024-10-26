def is_lambda(obj):
    return isinstance(obj, type(lambda: None)) and callable(obj)


class LandingGameActionEachFrame:
    """Callback defines an action that is triggered in each frame"""

    def __init__(self, action_callback: callable):
        self.action_callback = action_callback
        if not is_lambda(action_callback):
            raise TypeError(
                f"action_callback must be of type function, but is of type {type(action_callback)}"
            )

    def execute_action(self):
        self.action_callback()
