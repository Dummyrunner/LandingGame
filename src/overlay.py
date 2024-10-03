import pygame
from src.landing_game_object import LandingGameObject


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
        image: pygame.Surface,
        font: pygame.font.Font,
        alpha: int = 128,
        position=(0, 0),
    ):
        super().__init__(image, position)
        if not pygame.get_init():
            pygame.init()
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.font = font
        self.print_list = []

    def add_line(self, line) -> None:
        if isinstance(line, int):
            self.print_list.append(str(line))
        elif isinstance(line, float):
            self.print_list.append(str(line))
        elif isinstance(line, str):
            self.print_list.append(line)
        else:
            raise ValueError("Line must be of type int, float, or str")

    def normalize_attributes(
        self, attribute_name, attribute_display_name, attribute_format_as
    ) -> None:
        if attribute_name == None:
            raise ValueError("Attribute name must not be None")
        if not isinstance(attribute_name, str):
            raise ValueError("Attribute name must be a string")
        if attribute_display_name == None:
            attribute_display_name = attribute_name
        if attribute_format_as == None:
            attribute_format_as = str
        return attribute_name, attribute_display_name, attribute_format_as

    def format_line(
        self, obj, attribute_name, attribute_display_name, attribute_format_as
    ) -> str:
        if attribute_format_as == float:
            return (
                f"{attribute_display_name}: {float(obj.__dict__[attribute_name]):.2f}"
            )
        elif attribute_format_as == int:
            return f"{attribute_display_name}: {int(obj.__dict__[attribute_name])}"
        elif attribute_format_as == str:
            return f"{attribute_display_name}: {str(obj.__dict__[attribute_name])}"

    def add_attribute(
        self,
        obj: LandingGameObject,
        attribute_name: str,
        attribute_display_name: str,
        attribute_format_as: type,
    ) -> None:
        attribute_name, attribute_display_name, attribute_format_as = (
            self.normalize_attributes(
                attribute_name, attribute_display_name, attribute_format_as
            )
        )
        formatted_line = self.format_line(
            obj, attribute_name, attribute_display_name, attribute_format_as
        )
        self.add_line(formatted_line)

    def render_text(self, lines_ready_to_render) -> None:
        self.image.fill((0, 0, 0))
        line_number = 0

        for line in lines_ready_to_render:
            text_surface = self.font.render(line, True, (255, 255, 255))
            self.image.blit(text_surface, (0, line_number * self.font.get_height()))
            line_number += 1

    def update(self, time_step) -> None:
        self.render_text(self.print_list)
