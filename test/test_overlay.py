import unittest
import pygame
from src.overlay import Overlay
from src.landing_game_object import LandingGameObject
from src.game_statistics import GameStatistics


class TestOverlay(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.image = pygame.Surface((100, 100))
        self.font = pygame.font.SysFont("Calibri", 36)
        self.alpha = 128
        self.position = (10, 10)
        self.objects_to_display = [
            LandingGameObject(self.image, self.position),
            GameStatistics(),
        ]
        self.attributes_to_display = ["pos"]
        self.overlay = Overlay(
            self.image,
            self.font,
            self.alpha,
            self.position,
            self.objects_to_display,
            self.attributes_to_display,
        )

    def test_initialization(self):
        self.assertEqual(self.overlay.rect.topleft, self.position)
        self.assertEqual(self.overlay.font, self.font)
        self.assertEqual(self.overlay.objects_to_display, self.objects_to_display)

    def test_get_lines_ready_to_render(self):
        lines = self.overlay.get_lines_ready_to_render()
        self.assertIsInstance(lines, list)
        self.assertGreater(len(lines), 0)

    def test_get_desired_lines_from_object(self):
        obj = LandingGameObject(self.image, self.position)
        obj.pos = "(10, 10)"
        lines = self.overlay.get_desired_lines_from_object(
            obj, self.attributes_to_display
        )
        self.assertIn("pos=(10, 10)", lines)
