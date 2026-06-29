"""Core text rendering functionality for Pygame screens."""

from typing import Optional, Tuple, Union
import pygame


class TextConfig:
    """Configuration object for text rendering.

    Attributes:
        text: The text string to display
        x: X-coordinate position on screen
        y: Y-coordinate position on screen
        color: RGB tuple for text color (default: white)
        size: Font size in pixels (default: 24)
        font: Path to font file or None for system font (default: None)
        align: Text alignment - 'left', 'center', or 'right' (default: 'left')
        background_color: Optional RGB tuple for background color
        background_padding: Padding around text for background (default: 0)
    """

    def __init__(
        self,
        text: str,
        x: int,
        y: int,
        color: Tuple[int, int, int] = (255, 255, 255),
        size: int = 24,
        font: Optional[str] = None,
        align: str = "left",
        background_color: Optional[Tuple[int, int, int]] = None,
        background_padding: int = 0,
    ):
        """Initialize TextConfig.

        Args:
            text: The text string to display
            x: X-coordinate position
            y: Y-coordinate position
            color: RGB tuple for text color (default: white)
            size: Font size in pixels (default: 24)
            font: Font file path or None for system font (default: None)
            align: Text alignment ('left', 'center', 'right')
            background_color: Optional RGB tuple for background
            background_padding: Padding around text (default: 0)

        Raises:
            ValueError: If align is not 'left', 'center', or 'right'
        """
        if align not in ("left", "center", "right"):
            raise ValueError(f"align must be 'left', 'center', or 'right', got {align}")

        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font = font
        self.align = align
        self.background_color = background_color
        self.background_padding = background_padding


def print_text(
    surface: pygame.Surface,
    text: str,
    x: int,
    y: int,
    color: Tuple[int, int, int] = (255, 255, 255),
    size: int = 24,
    font: Optional[str] = None,
    align: str = "left",
    background_color: Optional[Tuple[int, int, int]] = None,
    background_padding: int = 0,
) -> pygame.Rect:
    """Render and display text on a Pygame surface.

    Args:
        surface: The Pygame surface to render text on
        text: The text string to display
        x: X-coordinate position
        y: Y-coordinate position
        color: RGB tuple for text color (default: white)
        size: Font size in pixels (default: 24)
        font: Font file path or None for system font (default: None)
        align: Text alignment ('left', 'center', 'right')
        background_color: Optional RGB tuple for background color
        background_padding: Padding around text for background (default: 0)

    Returns:
        pygame.Rect: Rectangle containing the rendered text

    Raises:
        ValueError: If align is not valid
        pygame.error: If font loading fails

    Example:
        >>> import pygame
        >>> pygame.init()
        >>> screen = pygame.display.set_mode((800, 600))
        >>> rect = print_text(
        ...     screen,
        ...     "Hello World",
        ...     x=50,
        ...     y=100,
        ...     color=(255, 0, 0),
        ...     size=32
        ... )
    """
    if align not in ("left", "center", "right"):
        raise ValueError(f"align must be 'left', 'center', or 'right', got {align}")

    # Create font object
    try:
        font_obj = pygame.font.Font(font, size)
    except pygame.error as e:
        raise pygame.error(f"Failed to load font {font}: {e}")

    # Render text
    text_surface = font_obj.render(text, True, color)
    text_rect = text_surface.get_rect()

    # Calculate position based on alignment
    if align == "center":
        text_rect.centerx = x
    elif align == "right":
        text_rect.right = x
    else:  # left
        text_rect.left = x

    text_rect.top = y

    # Handle background if specified
    if background_color is not None:
        bg_rect = text_rect.inflate(
            background_padding * 2, background_padding * 2
        )
        pygame.draw.rect(surface, background_color, bg_rect)

    # Blit text to surface
    surface.blit(text_surface, text_rect)

    return text_rect
