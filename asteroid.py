import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        child_angle = random.uniform(20.0, 50.0)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1_velocity = self.velocity.rotate(child_angle) * 1.2
        child_2_velocity = self.velocity.rotate(-child_angle) * 1.2
        child_1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_1.velocity = child_1_velocity
        child_2.velocity = child_2_velocity
