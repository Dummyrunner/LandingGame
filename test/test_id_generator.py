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

        self.id_generator.next_id = id2
        id3 = self.id_generator.assign_ID()
        assert id3 != id1, "IDs should be unique"

    def test_generate_rocket_id(self):
        rocket_id = self.id_generator.assign_rocket_ID()
        assert rocket_id == 0, "Rocket ID should be 0"
        with pytest.raises(ValueError):
            self.id_generator.assign_rocket_ID()
