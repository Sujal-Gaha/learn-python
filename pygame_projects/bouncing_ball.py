import pygame

# Constants
WIDTH, HEIGHT = 1000, 700
BLUE = "#0000FF"
WHITE = "#FFFFFF"
BALL_RADIUS = 30
BALL_INITIAL_VELOCITY = 0
GRAVITY = 0.3
FPS = 60

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

    def update(self):
        self.y += self.velocity
        self.velocity += self.acceleration

    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius, 0)
        
ball_one = Ball((WIDTH - (0.2 * WIDTH)) // 2, HEIGHT //2)
ball_two = Ball((WIDTH + (0.2 * WIDTH)) // 2, HEIGHT //2)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    ball_one.update()
    ball_two.update()

    ball_one.draw()
    ball_two.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()