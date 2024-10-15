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
    """

    def __init__(
        self,
        name: str,
        image: pygame.Surface,
        font: pygame.font.Font,
        position=(0, 0),
        alpha: int = Opacity.SEMI_TRANSPARENT,
    ):
        super().__init__(name, image, position)
        if not pygame.get_init():
            pygame.init()
        self.original_alpha = alpha
        self.image.set_alpha(self.original_alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.font = font
        self.line_order = []
        self.attached_object = None

    def update(self, *args) -> None:
        print_list = self.__get_printlist()
        self.__render_text(print_list)
        self.__update_position()

    def add_line(self, line) -> None:
        """Add a line to the overlay.

        Args:
            line (int or float or str): line to be added

        Raises:
            ValueError: unsupported line type
        """
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

    def attach_to_object(self, obj: LandingGameObject) -> None:
        self.attached_object = obj

    def detach_from_object(self) -> None:
        self.attached_object = None

    def hide(self) -> None:
        self.image.set_alpha(Opacity.TRANSPARENT)

    def show(self) -> None:
        self.image.set_alpha(self.original_alpha)

    def toggle_visibility(self) -> None:
        if self.image.get_alpha() == Opacity.TRANSPARENT:
            self.show()
        else:
            self.hide()

    def set_font(self, font: pygame.font.Font) -> None:
        self.font = font

    def reset_overlay(self) -> None:
        self.line_order = []

    def remove_first_line(self) -> None:
        if len(self.line_order) > 0:
            self.line_order.pop(0)

    def __update_position(self) -> None:
        if self.attached_object:
            self.rect.center = self.attached_object.rect.center

    def __normalize_attributes(
        self, attribute_name, attribute_display_name, attribute_format_as
    ) -> None:
        """Normalize attribute values.


        Args:
            attribute_name (_type_): _description_
            attribute_display_name (_type_): _description_
            attribute_format_as (_type_): _description_

        Raises:
            ValueError

        Returns:
            tuple: _attribute_name, attribute_display_name, attribute_format_as
        """
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
        """Format the attribute line by creating a string from display name and object data

        Args:
            obj (_type_): object to print info about within this overlay
            attribute_name (_type_)
            attribute_display_name (_type_)
            attribute_format_as (_type_)

        Returns:
            str: _description_
        """
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

    def __get_printlist(self) -> list:
        """Get the list of lines to be printed.


        Returns:
            list: _description_
        """
        print_list = []
        for line in self.line_order:
            if isinstance(line, str):
                print_list.append(line)
            elif isinstance(line, tuple):
                attribute_as_formatted_string = self.__get_line_from_object(*line)
                print_list.append(attribute_as_formatted_string)
        return print_list

    def __render_text(self, lines_ready_to_render: list[str] = [""]) -> None:
        """Render the text on the overlay.

        Args:
            lines_ready_to_render (list[str], optional): _description_. Defaults to [""].
        """
        self.image.fill((colors_dict["black"]))
        line_number = 0

        for line in lines_ready_to_render:
            text_surface = self.font.render(line, True, (colors_dict["white"]))
            self.image.blit(text_surface, (0, line_number * self.font.get_height()))
            line_number += 1
