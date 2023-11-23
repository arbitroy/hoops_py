import pygame

class Timer:
    def __init__(self, duration):
        # Initialize the timer with a given duration in milliseconds
        self.duration = duration
        # Record the start time using pygame's time module
        self.start_time = pygame.time.get_ticks()

    def get_time_left(self):
        # Calculate the elapsed time since the timer started
        elapsed_time = pygame.time.get_ticks() - self.start_time
        # Calculate the remaining time based on the duration and elapsed time
        time_left = max(0, self.duration - elapsed_time)
        return time_left

    def is_time_up(self):
        # Check if the timer has reached zero (time is up)
        return self.get_time_left() == 0
