import pytest
from unittest.mock import Mock, patch
from src.scenario_overlays import ScenarioOverlays
from src.colors import colors_dict
from src.overlay import Overlay
from src.game_timing import GameTiming
from src.surface_creator import create_pg_surface_from_color_and_size


@pytest.fixture
@patch("src.surface_creator.create_pg_surface_from_color_and_size")
def setup(mock_create_surface):
    mock_scenario = Mock()
    mock_object_list = Mock()
    mock_scenario.object_list = mock_object_list

    mock_ground = Mock()
    mock_ego = Mock()
    mock_kinematic = Mock()
    mock_ego.kinematic = mock_kinematic

    mock_game_timing = Mock(spec=GameTiming)
    mock_game_timing.time = 123.456

    mock_create_surface.return_value = Mock()

    return {
        "mock_scenario": mock_scenario,
        "mock_game_timing": mock_game_timing,
        "mock_ground": mock_ground,
        "mock_ego": mock_ego,
        "mock_kinematic": mock_kinematic,
    }


def test_create_overlays(setup):
    scenario_overlays = ScenarioOverlays(
        setup["mock_scenario"], setup["mock_game_timing"]
    )

    assert len(scenario_overlays.overlays) == 2

    debug_overlay = scenario_overlays.overlays[0]
    assert isinstance(debug_overlay, Overlay)

    hud_overlay = scenario_overlays.overlays[1]
    assert isinstance(hud_overlay, Overlay)
