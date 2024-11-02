import pygame
from pygame.locals import *
import sys


class EventHandler:
    def process_events(
        self, actions_each_frame, actions_while_key_pressed, actions_on_key_down
    ):
        self.__process_each_frame_events(actions_each_frame)
        self.__process_keyboard_events(actions_while_key_pressed, actions_on_key_down)

    def __process_keyboard_events(self, actions_while_key_pressed, actions_on_key_down):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.KEYDOWN:
                for action in actions_on_key_down:
                    if event.key == action.trigger_key.key_identifier:
                        action.execute_action()

        # check all key states and automatically perform all callbacks
        key_press_state = pygame.key.get_pressed()
        for action in actions_while_key_pressed:
            trigger_action_given: bool = (
                action.trigger_key.pressed
                == key_press_state[action.trigger_key.key_identifier]
            )
            if trigger_action_given:
                action.execute_action()

    def __process_each_frame_events(self, actions_each_frame):
        for act in actions_each_frame:
            act.execute_action()
