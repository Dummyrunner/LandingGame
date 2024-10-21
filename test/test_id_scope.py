import pytest
from src.id_scope import IDSCOPE


class MockObject:
    def __init__(self, id):
        self.id = id


@pytest.fixture
def scope():
    return IDSCOPE()


def test_create_standard_ids(scope):
    expected_ids = {
        "ego": 0,
        "ground": 1,
        "platform": 2,
    }
    assert scope.create_standard_ids() == expected_ids


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


def test_get_id_without_name(scope):
    obj1 = MockObject(4)
    obj2 = MockObject(5)
    scope.object_list = [obj1, obj2]
    assert scope.get_id() == 6


def test_get_id_with_name(scope):
    assert scope.get_id("ego") == 0
    assert scope.get_id("ground") == 1
    assert scope.get_id("platform") == 2


def test_get_id_with_nonexistent_name(scope):
    with pytest.raises(KeyError):
        scope.get_id("nonexistent")
