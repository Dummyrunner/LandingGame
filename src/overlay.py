import pygame
from src.landing_game_object import LandingGameObject
from src.linear_physical_object import LinearPhysicalObject
from src.game_statistics import GameStatistics


class Overlay(LandingGameObject):
    """
    Overlay that displays text on the screen. Takes a variety of different objects to display and renders them as text, depending on their type.

    Attributes:
        image (pygame.Surface): The surface on which the text will be rendered.
        position (tuple): The position of the overlay on the screen.
        objects_to_display (Union[pygame.sprite.Group, GameStatistics, dict, list, str]): The objects to display as text.
        font (pygame.font.Font): The font used to render the text.
        rect (pygame.Rect): The rectangle defining the position and size of the overlay.
        print_list (List[str]): The list of strings to be printed on the overlay.

    Methods:
        render_text(fontsize=16): Renders the text on the overlay.
        update(time_step): Updates the overlay.
    """

    def __init__(self, image, font, alpha, position=(0, 0), objects_to_display=None):
        super().__init__(image, position)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.font = font
        self.objects_to_display = objects_to_display

    def render_text(self, fontsize=16):
        self.image.fill((0, 0, 0))
        self.print_list = []
        line_number = 0

        if isinstance(self.objects_to_display, pygame.sprite.Group):
            for obj in self.objects_to_display:
                for attr, value in vars(obj).items():
                    self.print_list.append(f"{attr}={value}")
                self.print_list.append("")
        elif isinstance(self.objects_to_display, GameStatistics):
            for attr, value in vars(self.objects_to_display).items():
                if attr == "time" or "floattime":
                    self.print_list.append(f"{attr}={value}")
        elif isinstance(self.objects_to_display, dict):
            for key, value in self.objects_to_display.items():
                self.print_list.append(f"{key}={value}")
        elif isinstance(self.objects_to_display, list):
            for item in self.objects_to_display:
                self.print_list.append(str(item))
        elif isinstance(self.objects_to_display, str):
            self.print_list.append(self.objects_to_display)

        for line in self.print_list:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.image.blit(text_surface, (0, line_number * fontsize))
            line_number += 1

        print_list = None

    def get_lines(self) -> list[str]:
        objects_to_get_lines_from = []
        is_list = isinstance(self.objects_to_display, list)
        if is_list:
            for item in self.objects_to_display:
                if isinstance(item, LandingGameObject):
                    objects_to_get_lines_from.append(item)
        return self.print_list

    def update(self, time_step):
        lines = self.get_lines()
        self.render_text(lines)
