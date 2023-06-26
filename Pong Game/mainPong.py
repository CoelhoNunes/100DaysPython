from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time
import random

color = ["red", "orange", "yellow", "green", "blue", "purple", "orchid", "pink", "coral",
         "gold", "wheat", "cyan", "seashell", "moccasin", "goldenrod", "salmon", "ivory", "lime",
         "honeydew", "turquoise", "navy", "gray", "silver", "gainsboro", "firebrick", "maroon"]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG!")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.color(random.choice(color))
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.color(random.choice(color))
        ball.bounce_x()

    # Detect if the ball goes out of bounds (RIGHT SIDE)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if the ball goes out of bounds (LEFT SIDE)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
