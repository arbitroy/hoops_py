from BounceSurface import BounceSurface
import pygame
import numpy as np
from Ball import Ball2D
from Rim import Rim2D

class World:
    def __init__(self):
        # Initialize the game world with a basketball, rim, and other parameters

        # Create a basketball object
        self.ball = Ball2D("basketball.png", 15, 0.1).set_pos([70, 125])

        # Create a list to store rim objects
        self.rim = []

        # Coefficient of restitution
        self.e = 1.0  

        # Flag to track if a shot has been taken
        self.shot = False  

        # Single player's score
        self.score = 0  

        # Flag to track if the player has won
        self.won = False  

        # X-coordinate from which the shot was taken
        self.shot_from = 30  

        # Set a lifespan for the ball (in frames)
        self.ball_lifespan = 450  

        # Counter to track the ball's frames
        self.ball_frame_count = 0  

        # Create a bounce surface
        self.bounce_surface = BounceSurface(1280, 20)
        self.bounce_surface.rect.topleft = (0, 639)

        # Define sprite groups as instance variables
        self.ball_sprite_group = pygame.sprite.Group()
        self.bounce_surface_sprite_group = pygame.sprite.Group()

        # Add the ball and bounce surface to their respective sprite groups
        self.ball_sprite_group.add(self.ball)
        self.bounce_surface_sprite_group.add(self.bounce_surface)

    def reset(self, power):
        # Reset various game parameters, including the ball's position and power

        # Reset shot flag
        self.shot = False

        # Reset the ball's position
        self.ball = self.ball.set_pos([70, 125])

        # Reset the shot starting position
        self.shot_from = 30

        # Reset the ball's lifespan
        self.ball_lifespan = 450

        # Reset power
        power.reset()

        # Reset the ball's frame counter
        self.ball_frame_count = 0

    def update_score(self):
        # Update the player's score based on the shot's distance to the rim
        score = int((1030 - self.shot_from) / 100)
        self.score += score

        # Check if the player has won
        if self.score >= 30:
            self.won = True

    def add_rim(self, imgfile, radius):
        # Add a new rim to the game world and return the created rim object
        rim = Rim2D(imgfile, radius)
        self.rim.append(rim)
        return rim

    def draw(self, screen):
        # Draw game elements on the screen, including the ball, rims, and bounce surface

        # Check if the ball is in the specified coordinates
        ball_invisible_coordinates = (70, 125)
        if (
            ball_invisible_coordinates[0] - self.ball.radius <= self.ball.state[0] <= ball_invisible_coordinates[0] + self.ball.radius
            and ball_invisible_coordinates[1] - self.ball.radius <= self.ball.state[1] <= ball_invisible_coordinates[1] + self.ball.radius
        ):
            # Do not draw the ball if it is in the specified coordinates
            pass
        else:
            self.ball.draw(screen)

        # Draw rims
        for rim in self.rim:
            rim.draw(screen)

        # Draw the bounce surface
        screen.blit(self.bounce_surface.image, self.bounce_surface.rect)

    def update(self, dt, power):
        # Update the game state based on elapsed time and player input

        # Check for collisions with various game elements
        self.check_for_collision()

        # Update the ball's state
        self.ball.update(dt)

        # Check if the ball is out of bounds
        if (
            self.ball.state[0] > 1280 + self.ball.radius
            or self.ball.state[1] < 0 - self.ball.radius
        ):
            self.reset(power)

        # Check if the ball is in the rim
        top_of_ball = self.ball.state[1] + self.ball.radius
        if (
            self.ball.state[0] > 1000
            and self.ball.state[0] < 1075
            and top_of_ball > 295
            and top_of_ball < 305
        ):
            # Mark the shot as scored and update the score
            self.scored = True
            self.update_score()

        # Increment the frame count for the ball
        self.ball_frame_count += 1

        # Remove the ball if it exceeds its lifespan
        if self.ball_frame_count > self.ball_lifespan:
            self.reset(power)

    def normalize(self, v):
        # Normalize a vector to ensure it has unit length
        return v / np.linalg.norm(v)

    def check_for_collision(self):
        # Check for collisions with various game elements

        # Check for backboard collision
        if self.check_backboard_collision():
            return

        # Check for rim and surface collisions
        self.check_rim_collision()
        self.check_surface_collision()

    def check_backboard_collision(self):
        # Check for collision with the backboard and adjust ball velocity accordingly

        right_of_ball = self.ball.state[0] + self.ball.radius
        if right_of_ball >= 1075 and right_of_ball <= 1090:
            bottom_of_ball = self.ball.state[1] - self.ball.radius

            # Hit top of backboard
            if bottom_of_ball > 390 and bottom_of_ball <= 395:
                self.ball.state = self.ball.prev_state
                self.ball.set_vel([self.ball.state[2], -self.ball.state[3]])
                return True

            # Hit side of backboard
            if bottom_of_ball > 0 and bottom_of_ball <= 390:
                self.ball.state = self.ball.prev_state
                self.ball.set_vel([-self.ball.state[2], self.ball.state[3]])
                return True

        return False

    def check_surface_collision(self):
        # Check for collision with the bounce surface and update ball state accordingly

        # Calculate the top and bottom positions of the ball
        ball_top = 610 - self.ball.state[1]
        ball_bottom = ball_top + 2 * self.ball.radius

        # Check if the ball has collided with the bounce surface
        if ball_bottom > 635:
            # Ball has collided with the bounce surface
            self.ball.state[1] = 670 - 635 - self.ball.radius
            self.ball.state[3] = -self.ball.state[3] * self.e  # Reverse and dampen vertical velocity

            # Check if the vertical velocity is very low (below a threshold)
            threshold_velocity = 10  # Adjust this threshold as needed
            if abs(self.ball.state[3]) < threshold_velocity:
                self.ball_lifespan = 0
                self.ball.state[3] = 0

    def check_rim_collision(self):
        # Check for collision with the rim and handle the physics of the ball rebound

        pos_i = self.ball.state[0:2]
        for j in range(0, len(self.rim)):
            pos_j = np.array(self.rim[j].state[0:2])
            dist_ij = np.sqrt(np.sum((pos_i - pos_j) ** 2))

            radius_j = self.rim[j].radius
            if dist_ij > self.ball.radius + radius_j:
                continue

            self.ball.state = self.ball.prev_state

            vel_i = np.array(self.ball.state[2:])
            n_ij = self.normalize(pos_i - pos_j)

            mass_i = self.ball.mass

            J = -(1 + self.e) * np.dot(vel_i, n_ij) / ((1.0 / mass_i + 1.0))

            vel_i_aftercollision = vel_i + n_ij * J / mass_i

            self.ball.set_vel(vel_i_aftercollision)
            return
