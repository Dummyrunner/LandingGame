import pygame
import pytest
from src.overlay import Overlay


@pytest.fixture
def example_text():
    return "Hello, World!"


class TestOverlay:
    @pytest.fixture(autouse=True)
    def setup(self):
        pygame.init()
        self.position = (0, 0)
        self.obj_list = pygame.sprite.Group()
        self.image = pygame.Surface((200, 100))
        self.image.fill((0, 0, 0))

    def test_init(self, example_text):
        overlay = Overlay(self.image, self.position, self.obj_list)
        assert overlay.rect.topleft == self.position
        assert overlay.obj_list == self.obj_list

    def test_set_text(self, example_text):
        overlay = Overlay(self.image, self.position, self.obj_list)
        overlay.set_text(example_text)
        assert overlay.text == example_text

    def test_update(self, example_text):
        overlay = Overlay(self.image, self.position, self.obj_list)
        overlay.set_text(example_text)
        overlay.update(0.1)
        # Check if the text is rendered on the image
        text_surface = overlay.font.render(example_text, True, (255, 255, 255))
        overlay.image.blit(text_surface, (10, 10))
        assert overlay.image.get_at((10, 10)) == text_surface.get_at((0, 0))

    @pytest.fixture(autouse=True)
    def teardown(self):
        yield
        pygame.quit()


# Run the tests
if __name__ == "__main__":
    pytest.main()
