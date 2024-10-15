import pytest
from unittest.mock import MagicMock
from src.object_library import ObjectLibrary


class TestObjectLibrary:

    @pytest.fixture
    def object_library(self):
        return ObjectLibrary()

    def test_get_ID(self, object_library):
        id1 = object_library.get_ID()
        id2 = object_library.get_ID()
        assert id1 == 1
        assert id2 == 2

        object_library.next_ID = 1
        with pytest.raises(ValueError):
            id3 = object_library.get_ID()

    def test_get_used_IDs(self, object_library):
        object_library.get_ID()
        object_library.get_ID()
        used_ids = object_library.get_used_IDs()
        assert used_ids == [1, 2]

    def test_add_game_object(self, object_library):
        class MockObject:
            def __init__(self, name):
                self.name = name

        obj1 = MockObject("object1")
        object_library.add_game_object(obj1)
        assert "object1" in object_library.game_objects

        with pytest.raises(ValueError):
            object_library.add_game_object(obj1)

    def test_update(self, object_library):
        mock_object = MagicMock()
        mock_object.name = "object1"
        object_library.add_game_object(mock_object)
        object_library.update(0.1)
        mock_object.update.assert_called_once_with(0.1)

    def test_blit(self, object_library):
        mock_object = MagicMock()
        mock_object.name = "object1"
        object_library.add_game_object(mock_object)
        mock_display = MagicMock()
        object_library.blit(mock_display)
        mock_display.blit.assert_called_once_with(mock_object.image, mock_object.rect)
