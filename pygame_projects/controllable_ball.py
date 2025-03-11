import pygame
from enum import Enum

WIDTH, HEIGHT = 1000, 700
BLUE = "#0000FF"
WHITE = "#FFFFFF"
BALL_SPEED_X, BALL_SPEED_Y = 5, 5
BALL_RADIUS = 20
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Controllable Ball")
clock = pygame.time.Clock()

class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"
    NONE = "NONE"

class ControllableBall:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = BALL_RADIUS
        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def handle_ball(self, direction: Direction):
        if direction == Direction.NONE: return

        if direction == Direction.UP:
            self.y -= self.dy
        elif direction == Direction.DOWN:
            self.y += self.dy
        elif direction == Direction.LEFT:
            self.x -= self.dx
        elif direction == Direction.RIGHT:
            self.x += self.dx

    def generate(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)

direction = Direction.NONE

controllable_ball = ControllableBall()

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False   

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                direction = Direction.UP
            elif ev.key == pygame.K_DOWN:
                direction = Direction.DOWN
            elif ev.key == pygame.K_LEFT:
                direction = Direction.LEFT
            elif ev.key == pygame.K_RIGHT:
                direction = Direction.RIGHT
        elif ev.type == pygame.KEYUP:
            direction = Direction.NONE

    screen.fill(WHITE)

    controllable_ball.handle_ball(direction)
    controllable_ball.generate()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()