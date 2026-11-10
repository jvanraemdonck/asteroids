import pygame, sys
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

from logger import log_event

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def collides_with(self, other):
        if self.position.distance_to(other.position) < self.radius + other.radius:
            log_event("asteroid_shot")
            self.kill()
            other.split()
