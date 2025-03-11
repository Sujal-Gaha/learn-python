import pygame

WIDTH, HEIGHT = 1000, 700
WHITE="#FFFFFF"
RED = "#FF0000"
BALL_RADIUS = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Sprite")
clock = pygame.time.Clock()

class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = BALL_RADIUS
        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def update(self):
        self.y += self.dy

        print(f"${self.y} and {self.radius}")

        if self.y + self.radius == HEIGHT:
            self.dy = -self.dy

        if self.radius - self.y == 0:
            self.dy = abs(self.dy)

    def generate(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)


ball = Ball()

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    ball.update()
    ball.generate()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()