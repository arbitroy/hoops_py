import pygame


class BounceSurface(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))  # Set the surface color
        self.rect = self.image.get_rect()
