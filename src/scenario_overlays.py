from src.common_constants import CommonConstants, GameFonts, Opacity
from src.colors import colors_dict
from src.overlay import Overlay
from src.game_timing import GameTiming
from src.surface_creator import create_pg_surface_from_color_and_size


class ScenarioOverlays:
    def __init__(self, scenario, *args):
        self.scenario = scenario
        self.args = args
        self.overlays = self.create_overlays(scenario.object_list, args)

    def create_overlays(self, object_list, args):
        overlays = []
        debug_overlay = Overlay(
            create_pg_surface_from_color_and_size(
                colors_dict["black"], (CommonConstants.WINDOW_WIDTH / 3, 400)
            ),
            GameFonts.BASIC_FONT,
            (10, 10),
            Opacity.SEMI_TRANSPARENT,
        )
        debug_overlay.add_line("Debug Information:")
        debug_overlay.add_line("")
        debug_overlay.add_line("Ground")
        ground = object_list.get_object_by_name("ground")
        debug_overlay.add_attribute(ground, "pos", "Altitude", None)

        debug_overlay.add_line("")
        debug_overlay.add_line("Rocket")
        ego = object_list.get_object_by_name("ego")
        debug_overlay.add_attribute(ego, "pos", "Position", None)
        debug_overlay.add_attribute(ego.kinematic, "velocity", "Velocity", None)
        debug_overlay.add_attribute(
            ego.kinematic, "external_forces", "External Forces", None
        )
        debug_overlay.add_attribute(ego, "health", "Health: ", None)
        overlays.append(debug_overlay)

        hud_overlay = Overlay(
            create_pg_surface_from_color_and_size(
                colors_dict["black"], (CommonConstants.WINDOW_WIDTH - 20, 80)
            ),
            GameFonts.BASIC_FONT,
            (10, CommonConstants.WINDOW_HEIGHT - 90),
            Opacity.SEMI_TRANSPARENT,
        )
        for arg in args:
            if isinstance(arg, GameTiming):
                game_timing = arg
                break
        if game_timing is None:
            raise ValueError("GameTiming object not found in args")
        hud_overlay.add_attribute(game_timing, "time", "Time", float)
        overlays.append(hud_overlay)

        return overlays
