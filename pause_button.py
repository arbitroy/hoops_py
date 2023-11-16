import pygame

class PauseButton:
    def __init__(self, position, size):
        self.rect = pygame.Rect(position, size)
        self.color = (0, 0, 255)  # Blue color
        self.bar_color = (255, 255, 255)  # White color for bars

    def draw(self, screen):
        # Draw the blue background
        pygame.draw.rect(screen, self.color, self.rect)

        # Calculate the dimensions for the white bars
        bar_width = self.rect.width // 6
        bar_height = self.rect.height // 2

        # Adjust the position to move the bars a little more to the right
        bar_offset = self.rect.width // 6

        # Draw the first white bar
        bar1_rect = pygame.Rect(self.rect.left + bar_offset, self.rect.centery - bar_height // 2, bar_width, bar_height)
        pygame.draw.rect(screen, self.bar_color, bar1_rect)

        # Draw the second white bar
        bar2_rect = pygame.Rect(self.rect.left + 4 * bar_offset, self.rect.centery - bar_height // 2, bar_width, bar_height)
        pygame.draw.rect(screen, self.bar_color, bar2_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
