import pygame
import random

# Constants
HEIGHT, WIDTH = 700, 1000
RED,GREEN, BLUE = "#FF0000", "#00FF00", "#0000FF"
WHITE = "#FFFFFF"
BALL_RADIUS = 30
BALL_INITIAL_VELOCITY = 0
GRAVITY = 0.3
BOUNCE_DAMPING = 1.1 # Set to 0.8 means that the ball conserves 80% of its energy
FPS = 60
BALL_COUNT = 10

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball Simulation')
clock = pygame.time.Clock()

class Ball:
    def __init__(self, h, k):
        self.h = h
        self.k = k
        self.velocity = BALL_INITIAL_VELOCITY
        self.acceleration = GRAVITY
        self.radius = BALL_RADIUS
        self.color = random.choice([RED, GREEN, BLUE])
    
    def check_collission(self):
        pass

    def update(self):
        self.k += self.velocity
        self.velocity += self.acceleration

        print(f"{self.k}, {self.radius}, {self.velocity}, {self.acceleration}, {HEIGHT}")

        if (self.k + self.radius) >= HEIGHT:
            self.k = HEIGHT - self.radius
            self.velocity = -self.velocity * BOUNCE_DAMPING

            if abs(self.velocity) < 2:
                self.velocity = 0

        if (self.k + self.radius) <= 0:
            self.k += self.radius
            self.velocity = abs(self.velocity)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.h, self.k), self.radius, 0)
        
balls = [
     Ball(
        h=random.randint(100, WIDTH - 100),
        k=random.randint(100, HEIGHT // 2)
    ) 
    for _ in range(BALL_COUNT)
]

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for ball in balls:
        ball.update()
        ball.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()