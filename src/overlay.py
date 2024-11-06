import pygame
from src.landing_game_object import LandingGameObject
from src.linear_physical_object import LinearPhysicalObject
from src.colors import colors_dict
from src.common_constants import Opacity
from src.vec2d import Vec2d


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
        image: pygame.Surface,
        font: pygame.font.Font,
        position=(0, 0),
        alpha: int = Opacity.SEMI_TRANSPARENT,
    ):
        super().__init__(image, position)
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

        if hasattr(obj, attribute_name):
            self.line_order.append(
                (
                    obj,
                    attribute_name,
                    attribute_display_name,
                    attribute_format_as,
                )
            )
        else:
            self.line_order.append(f"Ovrl. Err.: attribute {attribute_name} not found")

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

    def __get_display_value_from_object(self, obj, attribute_name) -> str:
        """Get the display value from the object by checking if the attribute is present in the object or its kinematic object."""

        display_value = None
        if hasattr(obj, attribute_name):
            display_value = getattr(obj, attribute_name)
        else:
            return f"Ovrl. Err.: attribute {attribute_name} not found"

        if isinstance(display_value, Vec2d):
            display_value = f"Vec2d({display_value.x:.2f}, {display_value.y:.2f})"
        if isinstance(display_value, list) and all(
            isinstance(i, Vec2d) for i in display_value
        ):
            display_value = [
                f"Vec2d({force.x:.2f}, {force.y:.2f})" for force in display_value
            ]

        return display_value

    def __format_line(
        self,
        obj: LandingGameObject,
        attribute_name,
        attribute_display_name,
        attribute_format_as,
    ) -> str:
        """Format the attribute line by creating a string from display name and object data. Returns a "name not found" string,
        if attribute_name is not an attribute of obj.

        Args:
            obj: object to print info about within this overlay
            attribute_name (str)
            attribute_display_name (str)
            attribute_format_as (type (float, int, str))

        Returns:
            str: Attribute display name and value
        """

        display_value = self.__get_display_value_from_object(obj, attribute_name)
        formated_value = None

        if attribute_format_as == float:
            formated_value = round(display_value, 2)
        elif attribute_format_as == int:
            formated_value = int(display_value)
        elif attribute_format_as == str:
            formated_value = str(display_value)

        return f"{attribute_display_name}: {formated_value}"

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
        """Get the list of lines to be printed. Returns a list of strings to be printed on the overlay. If the line is a string, it is added to the list as is. If the line is a tuple, it is formatted as a string and added to the list."""
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
