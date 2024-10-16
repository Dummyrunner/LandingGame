import pytest
from src.id_generator import IDGenerator


class TestIDGenerator:

    def setup_method(self):
        self.id_generator = IDGenerator()

    def test_generate_id(self):
        id1 = self.id_generator.generate_id()
        id2 = self.id_generator.generate_id()
        assert id1 != id2, "IDs should be unique"
        assert isinstance(id1, str), "ID should be a string"
        assert isinstance(id2, str), "ID should be a string"

    def test_id_format(self):
        id = self.id_generator.generate_id()
        assert len(id) == 8, "ID should be 8 characters long"
        assert id.isalnum(), "ID should be alphanumeric"
