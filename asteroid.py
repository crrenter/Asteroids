from circleshape import CircleShape
import pygame
import random
from constants import PLAYER_RADIUS, LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid_a = self.velocity.rotate(angle)
        asteroid_b = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = asteroid_a * 1.2
        b = Asteroid(self.position.x, self.position.y, new_radius)
        b.velocity = asteroid_b * 1.2
