import pygame
import random
import math
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Generate points for asteroid shape
        self.points = []
        num_points = 8  # Number of vertices for the asteroid
        for i in range(num_points):
            angle = math.radians(i * (360 / num_points) + random.randint(-15, 15))
            r = radius + random.randint(-radius//3, radius//3)
            point_x = r * math.cos(angle)
            point_y = r * math.sin(angle)
            self.points.append((point_x, point_y))
    
    def draw(self, screen):
        # Transform points to screen coordinates
        screen_points = []
        for point_x, point_y in self.points:
            screen_points.append((self.position.x + point_x, self.position.y + point_y))


        pygame.draw.polygon(screen, COLOR_WHITE, screen_points, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):                                    # Splits the asteroid into smaller asteroids on hit. 
        self.kill()                                     

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = a * 1.2
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two.velocity = b * 1.2