# Print in Pygame's Screen

A Python library that enables easy text rendering and printing directly to a Pygame screen with customizable styling options.

## Features

- **Simple Text Rendering**: Easy-to-use functions for printing text on Pygame surfaces
- **Customizable Styling**: Control font, size, color, and positioning
- **Multiple Text Alignment**: Support for left, center, and right alignment
- **Background Support**: Optional backgrounds for text rendering
- **Flexible Integration**: Works seamlessly with existing Pygame projects

## Installation

```bash
pip install lib-print-in-pygame-s-screen
```

Or clone the repository:

```bash
git clone https://github.com/Loyam1/lib_print-in-pygame-s-screen.git
```

## Quick Start

```python
import pygame
from lib_print_in_pygame import print_text

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Print text to screen
print_text(screen, "Hello, Pygame!", x=100, y=50, color=(255, 255, 255), size=32)

pygame.display.flip()
```

## Usage

### Basic Text Rendering

```python
from lib_print_in_pygame import print_text

print_text(surface, text, x, y, color=(255, 255, 255), size=24, font=None)
```

**Parameters:**
- `surface`: The Pygame surface to render text on
- `text`: The text string to display
- `x`: X-coordinate position
- `y`: Y-coordinate position
- `color`: RGB tuple (default: white)
- `size`: Font size in pixels (default: 24)
- `font`: Font file path (default: system font)

### Advanced Options

```python
print_text(
    surface, 
    "Advanced Text",
    x=400,
    y=300,
    color=(255, 0, 0),
    size=48,
    font="path/to/font.ttf",
    align="center",  # "left", "center", or "right"
    background_color=(0, 0, 0),  # Optional background
    background_padding=10
)
```

## Requirements

- Python 3.6+
- Pygame 1.9.0+

## Examples

See the `examples/` directory for complete working examples.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/Loyam1/lib_print-in-pygame-s-screen/issues).

## Author

Created by Loyam1

---

Happy coding! 🎮
