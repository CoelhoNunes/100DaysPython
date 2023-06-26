from turtle import Turtle
import random

color = ["red", "orange", "yellow", "green", "blue", "purple", "orchid", "pink", "coral",
         "gold", "wheat", "cyan", "seashell", "moccasin", "goldenrod", "salmon", "ivory", "lime"
         "honeydew", "turquoise", "navy", "gray", "silver", "gainsboro", "firebrick", "maroon"]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(color))
        self.shape("turtle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
