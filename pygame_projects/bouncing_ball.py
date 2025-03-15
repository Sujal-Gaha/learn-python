import pygame
import random

# Constants
HEIGHT, WIDTH = 700, 1000
RED,GREEN, BLUE = "#FF0000", "#00FF00", "#0000FF"
WHITE = "#FFFFFF"
BALL_RADIUS = 30
BALL_INITIAL_VELOCITY = 0
GRAVITY = 0.3
BOUNCE_DAMPING = 0.8 # Set to 0.8 means that the ball conserves 80% of its energy
FPS = 60
BALL_COUNT = 20

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball Simulation')
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = BALL_INITIAL_VELOCITY
        self.acceleration = GRAVITY
        self.radius = BALL_RADIUS
        self.color = random.choice([RED, GREEN, BLUE])

    def update(self):
        self.y += self.velocity
        self.velocity += self.acceleration

        print(f"{self.y}, {self.radius}, {self.velocity}, {self.acceleration}, {HEIGHT}")

        if (self.y + self.radius) >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.velocity = -self.velocity * BOUNCE_DAMPING

            if abs(self.velocity) < 2:
                self.velocity = 0

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius, 0)
        
balls = [
     Ball(
        x=random.randint(100, WIDTH - 100),
        y=random.randint(100, HEIGHT // 2)
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