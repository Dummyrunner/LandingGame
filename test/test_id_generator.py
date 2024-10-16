import pytest
from src.id_generator import IDGenerator


class TestIDGenerator:

    def setup_method(self):
        self.id_generator = IDGenerator()

    def test_initialize(self):
        assert self.id_generator.current_id is not None
        assert self.id_generator.current_id >= 0
        assert isinstance(self.id_generator.current_id, int)

    def test_generate_id(self):
        id1 = self.id_generator.assign_ID()
        id2 = self.id_generator.assign_ID()
        assert id1 != id2, "IDs should be unique"
        assert isinstance(id1, int), "ID should be a integer"
        assert isinstance(id2, int), "ID should be a integer"
