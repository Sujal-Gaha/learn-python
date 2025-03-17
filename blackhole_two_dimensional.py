import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Black Hole properties
bh_x, bh_y = WIDTH // 2, HEIGHT // 2
bh_radius = 30

# Celestial body properties
orbit_radius = 200
angle = 0
speed = 0.02  # Speed of orbit

running = True
while running:
    screen.fill(BLACK)
    
    # Draw black hole
    pygame.draw.circle(screen, WHITE, (bh_x, bh_y), bh_radius)
    
    # Update orbiting body's position
    planet_x = int(bh_x + orbit_radius * np.cos(angle))
    planet_y = int(bh_y + orbit_radius * np.sin(angle))
    angle += speed
    
    # Draw orbiting body
    pygame.draw.circle(screen, YELLOW, (planet_x, planet_y), 10)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
