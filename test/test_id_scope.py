import pytest
import pygame

from src.id_scope import IDSCOPE
from src.landing_game_object import LandingGameObject


class MockObject(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def add_internal(self, group):
        pass

    def remove_internal(self, group):
        pass
        self.id = id

    def add_internal(self, group):
        pass

    def remove_internal(self, group):
        pass


@pytest.fixture
def scope():
    return IDSCOPE(pygame.sprite.Group())


def test_set_standard_ids(scope):
    standard_ids = {
        "ego": 0,
        "ground": 1,
        "platform": 2,
    }
    scope.set_standard_ids(standard_ids)
    assert scope.standard_ids == standard_ids


def test_set_standard_ids_already_set(scope):
    standard_ids = {
        "ego": 0,
        "ground": 1,
        "platform": 2,
    }
    scope.set_standard_ids(standard_ids)
    with pytest.raises(ValueError):
        scope.set_standard_ids(standard_ids)


def test_name_object_success(scope):
    obj = MockObject(3)
    scope.name_object(obj, "new_object")
    assert scope.name_to_id["new_object"] == 3


def test_name_object_name_already_in_use(scope):
    obj = MockObject(3)
    scope.name_object(obj, "new_object")
    with pytest.raises(ValueError):
        scope.name_object(obj, "new_object")


def test_name_object_id_already_in_use(scope):
    obj1 = MockObject(3)
    obj2 = MockObject(3)
    scope.name_object(obj1, "new_object")
    with pytest.raises(ValueError):
        scope.name_object(obj2, "another_object")


def test_create_id_without_name(scope):
    obj1 = MockObject(4)
    obj2 = MockObject(5)
    scope.add_object(obj1)
    scope.add_object(obj2)
    assert scope.create_id() == 6


def test_create_id_with_name(scope):
    standard_ids = {
        "ego": 0,
        "ground": 1,
        "platform": 2,
    }
    scope.set_standard_ids(standard_ids)
    assert scope.create_id("ego") == 0
    assert scope.create_id("ground") == 1
    assert scope.create_id("platform") == 2


def test_create_id_with_nonexistent_name(scope):
    standard_ids = {
        "ego": 0,
        "ground": 1,
        "platform": 2,
    }
    scope.set_standard_ids(standard_ids)
    with pytest.raises(KeyError):
        scope.create_id("nonexistent")


def test_add_object_success(scope):
    obj = MockObject(3)
    scope.add_object(obj)
    assert obj in scope.object_list


def test_add_object_id_already_in_list(scope):
    obj1 = MockObject(3)
    obj2 = MockObject(3)
    scope.add_object(obj1)
    with pytest.raises(ValueError):
        scope.add_object(obj2)
