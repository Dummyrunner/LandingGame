import pygame

from src.landing_game_group import LandingGameGroup
from src.vec2d import Vec2d
from src.common_constants import CommonConstants, Opacity
from src.colors import colors_dict
from src.general_physics import meter_to_pixel
from src.rocket import Rocket
from src.landing_game_object import LandingGameObject
from src.landing_game_action_on_key import LandingGameActionOnKey, PygameKeyState
from src.landing_game_action_periodic import LandingGameActionEachFrame
from src.surface_creator import create_pg_surface_from_color_and_size


class Scenario:
    def __init__(self):
        self.object_list = self.create_objects()
        self.action_dict = self.create_actions(self.object_list)
        (
            self.actions_each_frame,
            self.actions_while_key_pressed,
            self.actions_on_key_down,
        ) = self.create_key_bindings(self.action_dict)
        self.termination_condition = None

    def create_objects(self):
        object_list = LandingGameGroup()

        img_ego = create_pg_surface_from_color_and_size(
            colors_dict["red"],
            (meter_to_pixel(3.0), meter_to_pixel(8.0)),
        )
        rocket_pos = Vec2d(
            CommonConstants.WINDOW_WIDTH / 2, CommonConstants.WINDOW_HEIGHT / 2
        )
        rocket_mass = CommonConstants.ROCKET_MASS
        ego = Rocket(img_ego, rocket_pos, rocket_mass)
        object_list.add(ego)
        object_list.name_object("ego", ego)

        img_ground = create_pg_surface_from_color_and_size(
            colors_dict["green"], (CommonConstants.WINDOW_WIDTH, 10)
        )
        ground_position = Vec2d(CommonConstants.WINDOW_WIDTH / 2, 500)
        ground = LandingGameObject(img_ground, ground_position)
        object_list.add(ground)
        object_list.name_object("ground", ground)

        img_engine_fire = create_pg_surface_from_color_and_size(
            pygame.Color("orange"), CommonConstants.EXHAUST_FIRE_DOWN_DIMENSIONS
        )
        ego_engine_fire = LandingGameObject(
            img_engine_fire,
            pos=Vec2d(
                ego.rect.midbottom[0],
                ego.rect.midbottom[1]
                + 0.5 * CommonConstants.EXHAUST_FIRE_DOWN_DIMENSIONS.y,
            ),
        )
        object_list.add(ego_engine_fire)
        object_list.name_object("ego_engine_fire", ego_engine_fire)

        return object_list

    def create_actions(self, object_list):
        action_dict = {}

        ego = object_list.get_object_by_name("ego")
        activate_ego_upwards_boost = lambda: ego.activate_engine(
            CommonConstants.ROCKET_UPWARD_BOOST_FORCE_SCALAR * Vec2d(0, -1)
        )
        activate_left_engine_boost = lambda: ego.activate_engine(
            CommonConstants.ROCKET_SIDEWAYS_BOOST_FORCE_SCALAR * Vec2d(-1, 0)
        )
        activate_right_engine_boost = lambda: ego.activate_engine(
            CommonConstants.ROCKET_SIDEWAYS_BOOST_FORCE_SCALAR * Vec2d(1, 0)
        )

        ego_engine_fire = object_list.get_object_by_name("ego_engine_fire")
        hide_engine_fire_up = lambda: ego_engine_fire.set_color(
            pygame.Color("orange"),
            alpha=Opacity.TRANSPARENT,
        )
        show_engine_fire_up = lambda: ego_engine_fire.set_color(
            pygame.Color("orange"),
            alpha=Opacity.OPAQUE,
        )
        glue_engine_fire_down_to_ego = lambda: setattr(
            ego_engine_fire,
            "pos",
            Vec2d(
                ego.rect.midbottom[0],
                ego.rect.midbottom[1]
                + 0.5 * CommonConstants.EXHAUST_FIRE_DOWN_DIMENSIONS.y,
            ),
        )

        action_dict["activate_ego_upwards_boost"] = activate_ego_upwards_boost
        action_dict["activate_left_engine_boost"] = activate_left_engine_boost
        action_dict["activate_right_engine_boost"] = activate_right_engine_boost
        action_dict["hide_engine_fire_up"] = hide_engine_fire_up
        action_dict["show_engine_fire_up"] = show_engine_fire_up
        action_dict["glue_engine_fire_down_to_ego"] = glue_engine_fire_down_to_ego

        return action_dict

    def create_key_bindings(self, action_dict):
        actions_each_frame = []
        actions_while_key_pressed = []
        actions_on_key_down = []

        act_glue_exhaust_flame_up_to_ego = LandingGameActionEachFrame(
            action_dict["glue_engine_fire_down_to_ego"]
        )

        actions_each_frame.append(act_glue_exhaust_flame_up_to_ego)

        act_boost_ego_up_on_upwards_key = LandingGameActionOnKey(
            PygameKeyState(pygame.K_UP, True), action_dict["activate_ego_upwards_boost"]
        )
        act_boost_ego_left_on_left_key = LandingGameActionOnKey(
            PygameKeyState(pygame.K_LEFT, True),
            action_dict["activate_left_engine_boost"],
        )
        act_boost_ego_up_on_rigth_key = LandingGameActionOnKey(
            PygameKeyState(pygame.K_RIGHT, True),
            action_dict["activate_right_engine_boost"],
        )

        act_show_engine_fire_up_on_upwards_key = LandingGameActionOnKey(
            PygameKeyState(pygame.K_UP, True), action_dict["show_engine_fire_up"]
        )
        act_hide_engine_fire_up_on_upwards_key_not_pressed = LandingGameActionOnKey(
            PygameKeyState(pygame.K_UP, False), action_dict["hide_engine_fire_up"]
        )

        actions_while_key_pressed.append(act_boost_ego_up_on_upwards_key)
        actions_while_key_pressed.append(act_boost_ego_left_on_left_key)
        actions_while_key_pressed.append(act_boost_ego_up_on_rigth_key)
        actions_while_key_pressed.append(act_show_engine_fire_up_on_upwards_key)
        actions_while_key_pressed.append(
            act_hide_engine_fire_up_on_upwards_key_not_pressed
        )

        return actions_each_frame, actions_while_key_pressed, actions_on_key_down
