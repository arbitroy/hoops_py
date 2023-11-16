import pygame
import sys
from pygame.locals import *

MUSTARD = (255, 206, 72)  # Mustard color (RGB)
BLUE = (46, 44,153)  # BLUE color (RGB)

# Define your main menu function
def main_menu(screen):
    # Initialize the main menu variables
    font = pygame.font.Font(None, 36)
    selected_option = 0
    menu_options = ["Arcade", "Time trials", "Multiplayer", "Quit"]
    title = "Hoops"

    button_spacing = 40  # Adjust the spacing between buttons

    while True:
        # Handle user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        # Get the mouse position and button clicks
        mouse_x, mouse_y = pygame.mouse.get_pos()
        left_click, _, _ = pygame.mouse.get_pressed()

        if len(menu_options) > 0:
            button_width = screen.get_width() // len(menu_options) - button_spacing
        else:
            button_width = 0

        # Check if the mouse is over any menu option
        for i, option in enumerate(menu_options):
            text = font.render(option, True, (255, 255, 255) if i == selected_option else (100, 100, 100))
            text_rect = text.get_rect(center=(i * (button_width + button_spacing) + button_width / 2, screen.get_height() - 50))
            button_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)
            if button_rect.collidepoint(mouse_x, mouse_y):
                selected_option = i
                pygame.draw.rect(screen, MUSTARD, button_rect, border_radius=10)

        if left_click:
            if selected_option == 0:  # Arcade
                return
            elif selected_option == 1:  # Time trials
                return
            elif selected_option == 2:  # Multiplayer
                return
            elif selected_option == 3:  # Quit
                pygame.quit()
                sys.exit(0)

        # Set the background color to navy blue
        screen.fill(BLUE)

        # Display the title "Hoops" at the top half centered
        title_text = font.render(title, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 4))
        screen.blit(title_text, title_rect)

        # Display the menu options at the bottom with rounded, mustard-colored buttons
        for i, option in enumerate(menu_options):
            text = font.render(option, True, (255, 255, 255) if i == selected_option else (100, 100, 100))
            text_rect = text.get_rect(center=(i * (button_width + button_spacing) + button_width / 2, screen.get_height() - 50))
            button_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10)
            pygame.draw.rect(screen, MUSTARD, button_rect, border_radius=10)
            screen.blit(text, text_rect)

        pygame.display.update()

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((1280, 640))

# Call the main menu function
main_menu(screen)
