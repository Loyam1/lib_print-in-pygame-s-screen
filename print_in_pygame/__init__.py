"""Print in Pygame Screen - A library for text rendering in Pygame.

A Python library that enables easy text rendering and printing directly to a Pygame
screen with customizable styling options.

Example:
    Basic usage::

        import pygame
        from print_in_pygame import print_text

        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        print_text(
            screen,
            "Hello, Pygame!",
            x=100,
            y=50,
            color=(255, 255, 255),
            size=32
        )

        pygame.display.flip()
"""

__version__ = "0.2.0"
__author__ = "Loyam1"
__email__ = "mayol.picard@gmx.fr"
__license__ = "MIT"

from .print_in_screen import print_text, TextConfig

__all__ = ["print_text", "TextConfig", "__version__"]
