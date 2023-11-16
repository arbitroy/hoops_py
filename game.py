import sys
import pygame
from pygame.locals import *
from Ball import Ball2D
from World import World
from PowerBar import PowerBar
from Text import Text
from pause_button import PauseButton  # Import the pause button module

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

clock = pygame.time.Clock()

# Set the window dimensions
win_width = 1280
win_height = 640

# Create the game window
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Basketball")

# Load the background image
background_image = pygame.image.load("court.jpg").convert()

# Create a pause button instance
pause_button = PauseButton((win_width - 50, 10), (30, 30))  # Adjust size as needed

# Initialize game components
world = World()
power = PowerBar()
scoreboard = Text()

world.add_rim("disk-red.png", 5).set_pos([1000, 300])
world.add_rim("disk-red.png", 5).set_pos([1075, 300])

dt = 0.1

# Load a font for the pause menu
pause_font = pygame.font.Font(None, 36)

# Define a variable to track whether the game is paused
is_paused = False

# Modify the display_pause_menu function
def display_pause_menu(screen):
    overlay = pygame.Surface((win_width, win_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))

    resume_text_color = WHITE
    quit_text_color = WHITE

    resume_text = pause_font.render("Resume", True, resume_text_color)
    quit_text = pause_font.render("Quit", True, quit_text_color)

    resume_x = win_width // 2 - resume_text.get_width() // 2
    resume_y = win_height // 2 - resume_text.get_height()
    quit_x = win_width // 2 - quit_text.get_width() // 2
    quit_y = win_height // 2 + quit_text.get_height()

    mouse_x, mouse_y = 0, 0  # Initialize mouse coordinates

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos

            # Check if the user clicked on the "Resume" button
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if (
                    resume_x <= mouse_x <= resume_x + resume_text.get_width()
                    and resume_y <= mouse_y <= resume_y + resume_text.get_height()
                ):
                    return "resume"

                # Check if the user clicked on the "Quit" button
                elif (
                    quit_x <= mouse_x <= quit_x + quit_text.get_width()
                    and quit_y <= mouse_y <= quit_y + quit_text.get_height()
                ):
                    return "quit"

        # Check if the mouse is hovering over the "Resume" button
        if (
            resume_x <= mouse_x <= resume_x + resume_text.get_width()
            and resume_y <= mouse_y <= resume_y + resume_text.get_height()
        ):
            resume_text_color = (255, 0, 0)  # Change the color to red when hovering
        else:
            resume_text_color = WHITE  # Reset to white

        # Check if the mouse is hovering over the "Quit" button
        if (
            quit_x <= mouse_x <= quit_x + quit_text.get_width()
            and quit_y <= mouse_y <= quit_y + quit_text.get_height()
        ):
            quit_text_color = (255, 0, 0)  # Change the color to red when hovering
        else:
            quit_text_color = WHITE  # Reset to white

        resume_text = pause_font.render("Resume", True, resume_text_color)
        quit_text = pause_font.render("Quit", True, quit_text_color)

        # Draw the updated text
        screen.blit(overlay, (0, 0))
        screen.blit(resume_text, (resume_x, resume_y))
        screen.blit(quit_text, (quit_x, quit_y))
        pygame.display.update()

def main(screen):
    global is_paused
    while True:
        # Limit the frame rate to 60 FPS
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[K_p]:
            is_paused = not is_paused
            if is_paused:
                action = display_pause_menu(screen)
                if action == "resume":
                    is_paused = False
                elif action == "quit":
                    pygame.quit()
                    sys.exit(0)

        # Check if the pause button is clicked
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if pause_button.is_clicked((mouse_x, mouse_y)):
                is_paused = not is_paused
                if is_paused:
                    action = display_pause_menu(screen)
                    if action == "resume":
                        is_paused = False
                    elif action == "quit":
                        pygame.quit()
                        sys.exit(0)

        if is_paused:
            continue

        # Clear the background and draw the sprites
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        pause_button.draw(screen)
        world.draw(screen)
        power.draw(screen)
        
        pygame.draw.arc(screen, RED, (50, 50, 50, 50), 1, 1, 10)
        pygame.draw.line(screen, RED, [1000, 340], [1075, 340], 10)
        pygame.draw.line(screen, RED, [1075, 250], [1075, 640], 10)

        scoreboard.score_display(world, screen)

        if world.won:
            scoreboard.victory_message(world, screen)
            pygame.display.update()
            clock.tick(1)

            for i in range(100):
                pass

            break

        if not world.shot:
            power.start(world)
        else:
            won = world.update(dt, power)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main(screen)
