import pygame

pygame.init()

# Screen dimensions
screen_width, screen_height = 700, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Sort Visualization")

# Dimensions and values
x = 40
width = 20
height = [290, 120, 40, 200, 180, 300, 100, 20, 170, 70, 60, 30, 50, 110, 250, 80, 10, 90, 190, 160, 150]

# Colors
GREEN = (0, 255, 0)

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(screen, GREEN, (x + 30 * i, screen_height - height[i], width, height[i]))

running = True
sorting = False 
i, j = 0, 0     

while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not sorting:
        sorting = True 

    screen.fill((0, 0, 0)) 
    show(height)

    if sorting:
        if i < len(height) - 1:
            if j < len(height) - i - 1:
                if height[j] > height[j + 1]:
                    height[j], height[j + 1] = height[j + 1], height[j]
                j += 1
            else:
                j = 0
                i += 1
        else:
            sorting = False

        pygame.time.delay(20)

    pygame.display.update()

pygame.quit()