# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# tim.shape("turtle")
# tim.color("orange")
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# from turtle import Turtle, Screen, colormode
# import random
#
# color = colormode(255)
# tim = Turtle()
# tim.shape("turtle")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     all_colors = (r, g, b)
#     return all_colors


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed(0)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# my_screen = Screen()
# my_screen.exitonclick()

# Drawing the turtle into shapes
# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         tim.forward(100)
#         tim.right(angle)


# Drawing the turtle into shapes (2)
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# third Turtle - Circle thing
# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# tim.speed(0)
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)
#
# screen = t.Screen()
# screen.exitonclick()

# Spot painting

# import colorgram
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module


tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.hideturtle()

color_list = [(2, 13, 30), (52, 26, 18), (216, 129, 108),
              (13, 104, 157), (241, 212, 69), (150, 83, 40), (215, 88, 64), (164, 161, 34), (156, 8, 25),
              (156, 63, 102),
              (95, 6, 20), (12, 64, 33), (205, 75, 105), (174, 135, 160), (13, 94, 56), (2, 63, 144), (10, 175, 215),
              (155, 32, 23),
              (8, 211, 205), (11, 137, 86), (147, 226, 216), (121, 193, 150), (103, 219, 229), (221, 178, 214),
              (122, 169, 191), (80, 134, 178)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
