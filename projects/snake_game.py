from tkinter import *
import random
from enum import Enum

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50

SNAKE_COLOR = "#00FF00"
BODY_PARTS = 3
SPEED = 200

FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

def snake_game():
    window = Tk()

    class Direction(Enum):
        LEFT = "LEFT"
        RIGHT = "RIGHT"
        UP = "UP"
        DOWN = "DOWN"

    direction = Direction.DOWN
    score = 0

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE 
            y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

    def next_turn(snake: Snake, food: Food):
        x, y = snake.coordinates[0]

        if direction == Direction.UP:
            y -= SPACE_SIZE

        elif direction == Direction.DOWN:
            y += SPACE_SIZE

        elif direction == Direction.LEFT:
            x -= SPACE_SIZE

        elif direction == Direction.RIGHT:
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y)) 

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            nonlocal score

            score +=1

            label.config(text="Score{}".format(score))

            canvas.delete("food")

            food = Food()

        else:
            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        window.after(SPEED, next_turn, snake, food)

    def change_direction(new_direction):
        nonlocal direction

        if new_direction == Direction.LEFT and direction != Direction.RIGHT:
            direction = new_direction
        elif new_direction == Direction.RIGHT and direction != Direction.LEFT:
            direction = new_direction
        elif new_direction == Direction.UP and direction != Direction.DOWN:
            direction = new_direction
        elif new_direction == Direction.DOWN and direction != Direction.UP:
            direction = new_direction

    window.title("Snake Game")
    window.resizable(False, False)

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind('<Left>', lambda event: change_direction(Direction.LEFT))
    window.bind('<Right>', lambda event: change_direction(Direction.RIGHT))
    window.bind('<Up>', lambda event: change_direction(Direction.UP))
    window.bind('<Down>', lambda event: change_direction(Direction.DOWN))

    snake = Snake()
    food = Food()

    next_turn(snake, food)

    window.mainloop()