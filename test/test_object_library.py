import pytest
from unittest.mock import MagicMock
from src.object_library import ObjectIdentifier


class TestObjectIdentifier:

    @pytest.fixture
    def object_identifier(self):
        return ObjectIdentifier()

    def test_add_object(self, object_library):
        obj1 = MagicMock(name="object1")
        object_library.add_object(obj1)
        assert "object1" in object_library._objects_dict

    def test_add_object_duplicate(self, object_library):
        obj1 = MagicMock(name="object1")
        object_library.add_object(obj1)
        with pytest.raises(
            ValueError, match="Object with name object1 already exists."
        ):
            object_library.add_object(obj1)

    def test_get_ID(self, object_identifier):
        id1 = object_identifier.get_ID()
        id2 = object_identifier.get_ID()
        assert id1 == 1
        assert id2 == 2

    def test_get_used_IDs(self, object_identifier):
        object_identifier.get_ID()
        object_identifier.get_ID()
        used_ids = object_identifier.get_used_IDs()
        assert used_ids == [1, 2]

        class MockObject:
            def __init__(self, name):
                self.name = name
