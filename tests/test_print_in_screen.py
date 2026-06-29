"""Unit tests for print_in_screen module."""

import pytest
import pygame
from print_in_pygame import print_text, TextConfig


@pytest.fixture
def pygame_surface():
    """Fixture to create a Pygame surface for testing."""
    pygame.init()
    surface = pygame.Surface((800, 600))
    yield surface
    pygame.quit()


class TestTextConfig:
    """Tests for TextConfig class."""

    def test_text_config_creation(self):
        """Test creating a TextConfig object."""
        config = TextConfig(
            text="Hello",
            x=100,
            y=50,
            color=(255, 0, 0),
            size=32,
        )
        assert config.text == "Hello"
        assert config.x == 100
        assert config.y == 50
        assert config.color == (255, 0, 0)
        assert config.size == 32

    def test_text_config_defaults(self):
        """Test TextConfig default values."""
        config = TextConfig(text="Test", x=0, y=0)
        assert config.color == (255, 255, 255)
        assert config.size == 24
        assert config.font is None
        assert config.align == "left"
        assert config.background_color is None
        assert config.background_padding == 0

    def test_text_config_invalid_align(self):
        """Test TextConfig raises error for invalid alignment."""
        with pytest.raises(ValueError):
            TextConfig(
                text="Test",
                x=0,
                y=0,
                align="invalid",
            )

    def test_text_config_valid_alignments(self):
        """Test TextConfig with valid alignments."""
        for align in ["left", "center", "right"]:
            config = TextConfig(
                text="Test",
                x=0,
                y=0,
                align=align,
            )
            assert config.align == align


class TestPrintText:
    """Tests for print_text function."""

    def test_print_text_basic(self, pygame_surface):
        """Test basic text rendering."""
        rect = print_text(
            pygame_surface,
            "Hello World",
            x=50,
            y=50,
        )
        assert isinstance(rect, pygame.Rect)
        assert rect.x == 50
        assert rect.y == 50

    def test_print_text_with_custom_color(self, pygame_surface):
        """Test text rendering with custom color."""
        rect = print_text(
            pygame_surface,
            "Red Text",
            x=100,
            y=100,
            color=(255, 0, 0),
        )
        assert isinstance(rect, pygame.Rect)

    def test_print_text_with_custom_size(self, pygame_surface):
        """Test text rendering with custom font size."""
        rect = print_text(
            pygame_surface,
            "Big Text",
            x=50,
            y=50,
            size=48,
        )
        assert isinstance(rect, pygame.Rect)
        assert rect.height > 0

    def test_print_text_left_align(self, pygame_surface):
        """Test text rendering with left alignment."""
        rect = print_text(
            pygame_surface,
            "Left Aligned",
            x=100,
            y=50,
            align="left",
        )
        assert rect.left == 100

    def test_print_text_center_align(self, pygame_surface):
        """Test text rendering with center alignment."""
        rect = print_text(
            pygame_surface,
            "Center Aligned",
            x=400,
            y=50,
            align="center",
        )
        assert rect.centerx == 400

    def test_print_text_right_align(self, pygame_surface):
        """Test text rendering with right alignment."""
        rect = print_text(
            pygame_surface,
            "Right Aligned",
            x=750,
            y=50,
            align="right",
        )
        assert rect.right == 750

    def test_print_text_invalid_align(self, pygame_surface):
        """Test print_text raises error for invalid alignment."""
        with pytest.raises(ValueError):
            print_text(
                pygame_surface,
                "Invalid",
                x=0,
                y=0,
                align="invalid",
            )

    def test_print_text_with_background(self, pygame_surface):
        """Test text rendering with background."""
        rect = print_text(
            pygame_surface,
            "Text with Background",
            x=50,
            y=50,
            background_color=(0, 0, 0),
            background_padding=10,
        )
        assert isinstance(rect, pygame.Rect)

    def test_print_text_empty_string(self, pygame_surface):
        """Test text rendering with empty string."""
        rect = print_text(
            pygame_surface,
            "",
            x=50,
            y=50,
        )
        assert isinstance(rect, pygame.Rect)

    def test_print_text_unicode(self, pygame_surface):
        """Test text rendering with unicode characters."""
        rect = print_text(
            pygame_surface,
            "Hello 世界 🌍",
            x=50,
            y=50,
        )
        assert isinstance(rect, pygame.Rect)
