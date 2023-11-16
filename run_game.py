import os
import pygame

# Set the environment variable to hide the Pygame support prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'True'

# Import your main menu module
from main_menu import main_menu

# Import your game module
from game import main as run_game

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()

    # Set the window dimensions
    win_width = 1280
    win_height = 640

    # Create the game window
    screen = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Hoops")

    # Run the main menu
    main_menu(screen)

    # Start the game when the user selects "Start Game" in the main menu
    run_game(screen)
