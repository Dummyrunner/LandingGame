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

    def __init__(
        self,
        image,
        font,
        alpha,
        position=(0, 0),
        objects_to_display=None,
        attributes_to_display=None,
    ):
        super().__init__(image, position)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.font = font
        self.objects_to_display = objects_to_display
        attributes_to_display = attributes_to_display

    def render_text(self, lines_ready_to_render) -> None:
        self.image.fill((0, 0, 0))
        line_number = 0

        for line in lines_ready_to_render:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.image.blit(text_surface, (0, line_number * self.font.get_size()))
            line_number += 1

    def get_lines_ready_to_render(self) -> list[str]:
        if not isinstance(self.objects_to_display, list):
            self.objects_to_display = [self.objects_to_display]
        for obj in self.objects_to_display:
            for line in self.get_desired_lines_from_object(
                obj, attribuses_to_display=None
            ):
                self.print_list.append(line)
            return self.print_list

    def get_desired_lines_from_object(self, obj, attributes_to_display) -> list[str]:
        desired_lines = []
        if isinstance(obj, LandingGameObject):
            for attr, value in vars(obj).items():
                (
                    desired_lines.append(f"{attr}={value}")
                    if attr in attributes_to_display
                    else None
                )
            desired_lines.append("")
        elif isinstance(obj, GameStatistics):
            for attr, value in vars(obj).items():
                (
                    desired_lines.append(f"{attr}={value}")
                    if attr in attributes_to_display
                    else None
                )
        elif isinstance(obj, dict):
            for key, value in obj.items():
                (
                    desired_lines.append(f"{key}={value}")
                    if key in attributes_to_display
                    else None
                )
        elif isinstance(obj, list):
            for item in obj:
                desired_lines.append(str(item))
        elif isinstance(obj, str):
            desired_lines.append(obj)

        return desired_lines

    def update(self, time_step) -> None:
        lines_ready_to_render = self.get_lines_ready_to_render()
        self.render_text(lines_ready_to_render)
