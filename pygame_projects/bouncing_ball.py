import pygame
import random
import math

# Constants
HEIGHT, WIDTH = 700, 1000
FPS = 60

# Colors
WHITE = "#FFFFFF"
BLACK = "#000000"

RED, GREEN, BLUE = "#FF0000", "#00FF00", "#0000FF" # RGB
YELLOW, CYAN, MAGENTA = "#FFFF00", "#00FFFF", "#FF00FF"
ORANGE= "#FF7F00"

# Balls Config

BALL_RADIUS = 30
BALL_INITIAL_VELOCITY = 0
GRAVITY = 0.3
BOUNCE_DAMPING = 0.9 # Set to 0.8 means that the ball conserves 80% of its energy
BALL_COUNT = 20

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bouncing Ball Simulation')
clock = pygame.time.Clock()

class Ball:
    def __init__(self, h, k):
        self.h = h
        self.k = k
        self.velocity_y = BALL_INITIAL_VELOCITY
        self.velocity_x = random.uniform(-6, 6)
        self.acceleration = GRAVITY
        self.radius = BALL_RADIUS
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE])

    def check_collision(self, other_balls):
        for other_ball in other_balls:
            if other_ball == self:
                continue

            distance_betn_radii = math.sqrt(math.pow(self.h - other_ball.h, 2) + math.pow(self.k - other_ball.k, 2))
            sum_of_radii = self.radius + other_ball.radius

            print(f"${distance_betn_radii}, ${sum_of_radii}")

            if distance_betn_radii <= sum_of_radii:
                pass

    def update(self, balls):
        self.h += self.velocity_x
        self.k += self.velocity_y
        self.velocity_y += self.acceleration

        # print(f"{self.h}, {self.k}, {self.radius},{self.velocity_x}, {self.velocity_y}")

        if (self.k + self.radius) >= HEIGHT:
            self.k = HEIGHT - self.radius
            self.velocity_y = -self.velocity_y * BOUNCE_DAMPING

            if abs(self.velocity_y) < 2:
                self.velocity_y = 0

        if (self.k + self.radius) <= 0:
            self.k += self.radius
            self.velocity_y = abs(self.velocity_y)

        if (self.h + self.radius) >= WIDTH:
            self.h = WIDTH - self.radius
            self.velocity_x = -self.velocity_x

        if (self.h - self.radius) <= 0:
            self.h = self.radius
            self.velocity_x = abs(self.velocity_x)

        self.check_collision(balls)

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
        ball.update(balls)
        ball.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()