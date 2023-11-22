import pygame

class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = pygame.time.get_ticks()

    def get_time_left(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        time_left = max(0, self.duration - elapsed_time)
        return time_left

    def is_time_up(self):
        return self.get_time_left() == 0
