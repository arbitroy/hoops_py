import pygame
import numpy as np
from scipy.integrate import ode

class Ball2D(pygame.sprite.Sprite):
    def __init__(self, imgfile, radius, mass=1.0):
        pygame.sprite.Sprite.__init__(self)

        # Load the ball image and scale it
        self.image = pygame.image.load(imgfile)
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))

        # Set initial attributes and state
        self.rect = self.image.get_rect()
        self.state = [0, 0, 0, 0]
        self.prev_state = [0, 0, 0, 0]
        self.mass = mass
        self.t = 0
        self.radius = radius
        self.friction = 0.0001
        self.g = 9.8

        # Set up the solver for numerical integration
        self.solver = ode(self.f)
        self.solver.set_integrator("dop853")
        self.solver.set_f_params(self.friction, self.g)
        self.solver.set_initial_value(self.state, self.t)

    def f(self, t, state, arg1, arg2):
        # Define the differential equations for motion
        dx = state[2]
        dy = state[3]
        dvx = -state[2] * arg1
        dvy = -arg2 - state[3] * arg1
        dx += dvx
        dy += dvy
        return [dx, dy, dvx, dvy]

    def set_pos(self, pos):
        # Set the position of the ball
        self.state[0:2] = pos
        self.solver.set_initial_value(self.state, self.t)
        return self

    def set_vel(self, vel):
        # Set the velocity of the ball
        self.state[2:] = vel
        self.solver.set_initial_value(self.state, self.t)
        return self

    def update(self, dt):
        # Update the ball's state through numerical integration
        self.t += dt
        self.prev_state = self.state[:]
        self.state = self.solver.integrate(self.t)

    def move_by(self, delta):
        # Move the ball by a specified displacement
        self.prev_state = self.state[:]
        self.state[0:2] = np.add(self.state[0:2], delta)
        return self

    def draw(self, surface):
        # Draw the ball on the specified surface
        rect = self.image.get_rect()
        rect.center = (self.state[0], 640 - self.state[1])  # Flipping y
        surface.blit(self.image, rect)
