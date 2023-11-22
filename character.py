import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, position, idle_image, aim_image, shoot_image, scale_factor=0.2):
        super().__init__()

        self.idle_image = pygame.image.load(idle_image).convert_alpha()
        self.aim_image = pygame.image.load(aim_image).convert_alpha()
        self.shoot_image = pygame.image.load(shoot_image).convert_alpha()

        # Scale images
        self.idle_image = pygame.transform.scale(self.idle_image, (int(self.idle_image.get_width() * scale_factor), int(self.idle_image.get_height() * scale_factor)))
        self.aim_image = pygame.transform.scale(self.aim_image, (int(self.aim_image.get_width() * scale_factor), int(self.aim_image.get_height() * scale_factor)))
        self.shoot_image = pygame.transform.scale(self.shoot_image, (int(self.shoot_image.get_width() * scale_factor), int(self.shoot_image.get_height() * scale_factor)))

        self.image = self.idle_image  # Start with idle image
        self.rect = self.image.get_rect(topleft=position)
        self.is_shooting = False  # Add a flag to track shooting state

    def update(self, is_shooting):  
        self.is_shooting = is_shooting

        # Update logic here if needed
        if self.is_shooting:
            self.image = self.shoot_image
        else:
            self.image = self.aim_image if pygame.mouse.get_focused() else self.idle_image

    def draw(self, screen):
        screen.blit(self.image, self.rect)
