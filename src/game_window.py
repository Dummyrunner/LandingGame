import pygame
from src.common_constants import CommonConstants
from colors import colors


class GameWindow:
    def __init__(self, title):
        self.width = CommonConstants.WINDOW_WIDTH
        self.height = CommonConstants.WINDOW_HEIGHT
        self.title = title
        self.display = pygame.display.set_mode((self.width, self.height))
        self.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.fps = CommonConstants.FPS
        self.is_running = True

    def set_caption(self, title):
        pygame.display.set_caption(title)

    def erase_screen(self):
        self.window.fill(colors["white"])
