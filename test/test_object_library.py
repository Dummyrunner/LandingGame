import pytest
from unittest.mock import MagicMock
from src.object_library import ObjectIdentifier


class TestObjectIdentifier:

    @pytest.fixture
    def object_identifier(self):
        return ObjectIdentifier()

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
