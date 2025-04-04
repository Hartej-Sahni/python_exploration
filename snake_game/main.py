from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.snake_blocks[0].distance(food) < 15):
        food.refresh()
        scoreboard.refresh()
        snake.extend()
    if snake.hit_wall() or snake.hit_tail():
        scoreboard.reset()
        snake.reset()
        screen.update()

screen.exitonclick()