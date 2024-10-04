import pygame
from src.landing_game_object import LandingGameObject
from src.colors import colors_dict
from src.common_constants import Opacity


class Overlay(LandingGameObject):
    """
    Overlay class to display information on the screen.

    Attributes:
        image (pygame.Surface): The surface of the overlay.
        font (pygame.font.Font): The font used for the text.
        alpha (int): The transparency of the overlay.
        position (tuple): The position of the overlay.
        rect (pygame.Rect): The rectangle of the overlay.
        line_order (list): The order of the lines to be displayed.
        print_list (list): The list of lines to be printed.

    Methods:
        update(time_step): Update the overlay.
        add_line(line): Add a line to the overlay.
        add_attribute(obj, attribute_name, attribute_display_name, attribute_format_as): Add an attribute to the overlay.
        __normalize_attributes(attribute_name, attribute_display_name, attribute_format_as): Normalize the attribute values.
        __format_line(obj, attribute_name, attribute_display_name, attribute_format_as): Format the attribute line.
        __get_line_from_object(obj, attribute_name, attribute_display_name, attribute_format_as): Get the line from the object.
        __get_printlist(): Get the list of lines to be printed.
        __render_text(lines_ready_to_render): Render the text on the overlay.
    """

    def __init__(
        self,
        image: pygame.Surface,
        font: pygame.font.Font,
        position=(0, 0),
        alpha: int = Opacity.SEMI_TRANSPARENT,
    ):
        super().__init__(image, position)
        if not pygame.get_init():
            pygame.init()
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.font = font
        self.line_order = []
        self.attached_object = None

    def update(self, time_step) -> None:
        """
        Update the overlay.
        """
        print_list = self.__get_printlist()
        self.__render_text(print_list)
        self.__update_position()

    def add_line(self, line) -> None:
        if isinstance(line, int) or isinstance(line, float) or isinstance(line, str):
            self.line_order.append(str(line))
        else:
            raise ValueError("Line must be of type int, float, or str")

    def add_attribute(
        self,
        obj: LandingGameObject,
        attribute_name: str,
        attribute_display_name: str,
        attribute_format_as: type,
    ) -> None:
        """Add an attribute to the overlay. The attribute can be formatted as int, float, or str."""
        self.line_order.append(
            (obj, attribute_name, attribute_display_name, attribute_format_as)
        )

    def __update_position(self) -> None:
        if self.attached_object:
            self.rect.center = self.attached_object.rect.center

    def __normalize_attributes(
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

    def __format_line(
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

    def __get_line_from_object(
        self, obj, attribute_name, attribute_display_name, attribute_format_as
    ) -> str:
        attribute_name, attribute_display_name, attribute_format_as = (
            self.__normalize_attributes(
                attribute_name, attribute_display_name, attribute_format_as
            )
        )
        formatted_line = self.__format_line(
            obj, attribute_name, attribute_display_name, attribute_format_as
        )
        return formatted_line

    def __get_printlist(self) -> None:
        print_list = []
        for line in self.line_order:
            if isinstance(line, str):
                print_list.append(line)
            elif isinstance(line, tuple):
                attribute_as_formatted_string = self.__get_line_from_object(*line)
                print_list.append(attribute_as_formatted_string)
        return print_list

    def __render_text(self, lines_ready_to_render: list[str] = [""]) -> None:
        self.image.fill((colors_dict["black"]))
        line_number = 0

        for line in lines_ready_to_render:
            text_surface = self.font.render(line, True, (colors_dict["white"]))
            self.image.blit(text_surface, (0, line_number * self.font.get_height()))
            line_number += 1
