import pygame
import numpy as np

WIDTH, HEIGHT = 800, 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class BlackHole:
    def __init__(self, bh_x, bh_y, bh_radius):
        self.x = bh_x;
        self.y = bh_y;
        self.radius = bh_radius;

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius)

class CelestialBody:
    def __init__(self, color, orbit_radius, speed, size):
        self.color = color
        self.orbit_radius = orbit_radius
        self.speed = speed
        self.size = size
        self.angle = 0

    def update_position(self, center_x, center_y):
        self.x = int(center_x + self.orbit_radius * np.cos(self.angle))
        self.y = int(center_y + self.orbit_radius * np.sin(self.angle))
        self.angle += self.speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

blackhole = BlackHole(WIDTH // 2, HEIGHT // 2, 20)

planet = CelestialBody(YELLOW, orbit_radius=200, speed=0.02, size=10)

running = True
while running:
    screen.fill(WHITE)

    blackhole.draw()
        
    planet.update_position(blackhole.x, blackhole.y)
    planet.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
