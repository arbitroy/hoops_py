import pygame

class Rim2D(pygame.sprite.Sprite):
    def __init__(self, imgfile, radius):
        pygame.sprite.Sprite.__init__(self)

        # Load the image and scale it
        self.image = pygame.image.load(imgfile)
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))

        # Set the radius and initial state
        self.radius = radius
        self.state = [0, 0, 0, 0]

    def set_pos(self, pos):
        # Set the position of the rim
        self.state[0:2] = pos
        return self

    def draw(self, surface):
        # Draw the rim on the specified surface
        rect = self.image.get_rect()
        rect.center = (self.state[0], 640 - self.state[1])  # Flipping y
        surface.blit(self.image, rect)
