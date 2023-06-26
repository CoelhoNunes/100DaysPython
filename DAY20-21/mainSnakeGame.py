from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
import time
import random

color = ["red", "orange", "yellow", "green", "blue", "purple"]
colors = list(color)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
# CTRL + CMD + Space -> Emoji
screen.title("🐍🐍 THE SNAKE GAME 🐍🐍")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
for _ in color:
    random.choice(colors)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.reset()
        snake.reset()

    # Detect collision with tail
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreBoard.reset()
            snake.reset()
screen.exitonclick()
