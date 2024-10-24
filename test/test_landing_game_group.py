import pytest
import pygame
from src.landing_game_group import LandingGameGroup


@pytest.fixture
def group():
    pygame.init()
    group = LandingGameGroup()
    yield group
    pygame.quit()


@pytest.fixture
def sprites():
    sprite1 = pygame.sprite.Sprite()
    sprite2 = pygame.sprite.Sprite()
    return sprite1, sprite2


def test_name_object(group, sprites):
    sprite1, _ = sprites
    group.add(sprite1)
    group.name_object("sprite1", sprite1)
    assert group.get_object_by_name("sprite1") is sprite1


def test_name_object_not_in_group(group):
    sprite3 = pygame.sprite.Sprite()
    with pytest.raises(ValueError):
        group.name_object("sprite3", sprite3)


def test_name_object_name_already_in_use(group, sprites):
    sprite1, sprite2 = sprites
    group.add(sprite1, sprite2)
    group.name_object("sprite1", sprite1)
    with pytest.raises(ValueError):
        group.name_object("sprite1", sprite2)


def test_get_object_by_name(group, sprites):
    sprite1, _ = sprites
    group.add(sprite1)
    group.name_object("sprite1", sprite1)
    assert group.get_object_by_name("sprite1") == sprite1


def test_remove_object_by_name(group, sprites):
    sprite1, _ = sprites
    group.add(sprite1)
    group.name_object("sprite1", sprite1)
    group.remove_object_by_name("sprite1")
    with pytest.raises(KeyError):
        group.get_object_by_name("sprite1")


def test_remove(group, sprites):
    sprite1, _ = sprites
    group.add(sprite1)
    group.name_object("sprite1", sprite1)
    group.remove(sprite1)
    with pytest.raises(KeyError):
        group.get_object_by_name("sprite1")


def test_add_sprites(group, sprites):
    sprite1, sprite2 = sprites
    group.add(sprite1, sprite2)
    assert sprite1 in group
    assert sprite2 in group


def test_remove_sprites(group, sprites):
    sprite1, sprite2 = sprites
    group.add(sprite1, sprite2)
    group.remove(sprite1)
    assert sprite1 not in group
    assert sprite2 in group


def test_clear_group(group, sprites):
    sprite1, sprite2 = sprites
    group.add(sprite1, sprite2)
    group.empty()
    assert len(group) == 0
    with pytest.raises(KeyError):
        group.get_object_by_name("sprite1")
    with pytest.raises(KeyError):
        group.get_object_by_name("sprite2")


def test_get_object_by_id(group, sprites):
    sprite1, _ = sprites
    sprite1.id = 1
    group.add(sprite1)
    assert group.get_object_by_id(1) == sprite1


def test_get_object_by_id_not_found(group, sprites):
    sprite1, _ = sprites
    sprite1.id = 1
    group.add(sprite1)
    with pytest.raises(ValueError):
        group.get_object_by_id(2)


def test_remove_object_by_id(group, sprites):
    sprite1, _ = sprites
    sprite1.id = 1
    group.add(sprite1)
    group.remove_object_by_id(1)
    assert sprite1 not in group


def test_remove_object_by_id_not_found(group, sprites):
    sprite1, _ = sprites
    sprite1.id = 1
    group.add(sprite1)
    with pytest.raises(ValueError):
        group.remove_object_by_id(2)
