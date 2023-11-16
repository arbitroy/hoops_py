import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Text:
    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def score_display(self, world, screen):
        self.add_to_screen(screen, 30, "Player Score: " + str(world.score), 150, 50, RED)

    def victory_message(self, world, screen):
        winner = world.score
        self.add_to_screen(
            screen, 100, "Your score is " + str(winner) + "!", 640, 320
        )

    def add_to_screen(self, screen, font_size, text, center_x, center_y, color):
        largeText = pygame.font.Font("freesansbold.ttf", font_size)
        TextSurf, TextRect = self.text_objects(text, largeText, color)
        TextRect.center = (center_x, center_y)
        screen.blit(TextSurf, TextRect)
