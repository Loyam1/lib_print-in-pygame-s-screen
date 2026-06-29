"""Advanced example showcasing more features of print_in_pygame."""

import pygame
import math
from print_in_pygame import print_text, TextConfig


def main():
    """Run an advanced example with animations and multiple styles."""
    pygame.init()
    
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Print in Pygame - Advanced Example")
    clock = pygame.time.Clock()
    
    # Variables for animation
    frame = 0
    font_sizes = [20, 30, 40, 30, 20]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        frame += 1
        screen.fill((20, 20, 40))
        
        # Title with gradient effect (simulated by changing colors)
        colors = [
            (255, 0, 0),      # Red
            (255, 127, 0),    # Orange
            (255, 255, 0),    # Yellow
            (0, 255, 0),      # Green
            (0, 0, 255),      # Blue
        ]
        
        title = "Advanced Text Rendering"
        text_width = len(title) * 15  # Approximate
        start_x = (1024 - text_width) // 2
        char_x = start_x
        
        for i, char in enumerate(title):
            color = colors[i % len(colors)]
            print_text(
                screen,
                char,
                x=char_x,
                y=50,
                color=color,
                size=32,
            )
            char_x += 15
        
        # Animated font size
        y_pos = 150
        for i, size in enumerate(font_sizes):
            current_size = int(size + 5 * math.sin(frame / 30 + i))
            print_text(
                screen,
                f"Dynamic Size {i+1}",
                x=512,
                y=y_pos,
                size=max(10, current_size),
                color=(100 + i * 30, 150, 200),
                align="center",
            )
            y_pos += 60
        
        # FPS counter
        fps = int(clock.get_fps())
        print_text(
            screen,
            f"FPS: {fps}",
            x=10,
            y=10,
            color=(0, 255, 0),
            size=16,
        )
        
        # Instructions
        print_text(
            screen,
            "Close window to exit",
            x=512,
            y=700,
            color=(200, 200, 200),
            size=18,
            align="center",
            background_color=(40, 40, 60),
            background_padding=8,
        )
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    main()
