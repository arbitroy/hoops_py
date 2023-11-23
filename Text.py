import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Text:
    def text_objects(self, text, font, color):
        # Create a text surface and rectangle
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def score_display(self, world, screen):
        # Display the player's score on the screen
        self.add_to_screen(screen, 30, "Player Score: " + str(world.score), 150, 50, RED)

    def timer_display(self, screen, timer_value, center_x, center_y, color):
        # Display the timer value on the screen
        timer_text = f"Time: {timer_value // 1000}"  # Convert milliseconds to seconds
        self.add_to_screen(screen, 30, timer_text, center_x, center_y, color)

    def victory_message(self, world, screen):
        # Display a victory message on the screen
        winner = world.score
        self.add_to_screen(
            screen, 100, "Your score is " + str(winner) + "!", 640, 320, RED
        )

    def lose_message(self, screen, center_x, center_y, color):
        # Display a lose message on the screen
        message = "You Lose!"
        self.add_to_screen(screen, 50, message, center_x, center_y, color)

    def add_to_screen(self, screen, font_size, text, center_x, center_y, color):
        # Add text to the screen with specified font size, position, and color
        large_text = pygame.font.Font("freesansbold.ttf", font_size)
        text_surface, text_rect = self.text_objects(text, large_text, color)
        text_rect.center = (center_x, center_y)
        screen.blit(text_surface, text_rect)
