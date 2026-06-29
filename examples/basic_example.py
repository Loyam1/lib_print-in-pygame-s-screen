"""Basic example of using print_in_pygame library."""

import pygame
from print_in_pygame import print_text


def main():
    """Run a basic example of text rendering in Pygame."""
    # Initialize Pygame
    pygame.init()
    
    # Create display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Print in Pygame - Basic Example")
    
    # Create a clock to control frame rate
    clock = pygame.time.Clock()
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Print various texts
        print_text(
            screen,
            "Hello, Pygame!",
            x=400,
            y=50,
            color=(255, 255, 255),
            size=48,
            align="center"
        )
        
        print_text(
            screen,
            "This is a basic example",
            x=400,
            y=150,
            color=(100, 200, 255),
            size=24,
            align="center"
        )
        
        print_text(
            screen,
            "Left aligned text",
            x=50,
            y=250,
            color=(255, 100, 100),
            size=20,
            align="left"
        )
        
        print_text(
            screen,
            "Right aligned text",
            x=750,
            y=250,
            color=(100, 255, 100),
            size=20,
            align="right"
        )
        
        print_text(
            screen,
            "Text with background",
            x=400,
            y=350,
            color=(255, 255, 255),
            size=20,
            background_color=(50, 50, 50),
            background_padding=10,
            align="center"
        )
        
        print_text(
            screen,
            "Close this window to exit",
            x=400,
            y=500,
            color=(150, 150, 150),
            size=16,
            align="center"
        )
        
        # Update display
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
    
    pygame.quit()


if __name__ == "__main__":
    main()
