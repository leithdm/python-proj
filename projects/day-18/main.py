import turtle as t
import colorgram
from turtle import Screen
import random

# extract colors from .jpg using colorgram
# colors = colorgram.extract('hirst.jpg', 30)
# color_array = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_array.append(color_tuple)
# print(color_array)

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
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







# starter-code to draw a square, polygons, and a spiral

# draw a square
# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# for _ in range(10):
#     t.pendown()
#     t.forward(10)
#     t.penup()
#     t.forward(10)

# draw polygons
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.forward(100)
#         t.right(angle)
#
#
# for num in range(3, 10):
#     draw_shape(num)


# draw a colored random-walk
# directions = [0, 90, 180, 270]
# turtle.pensize(10)
# turtle.speed("fastest")
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_c = (r, g, b)
#     return random_c
#
#
# for _ in range(200):
#     turtle.pencolor(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))

# draw a spiral
# turtle.speed("fastest")
# turtle.pendown()
#
# for _ in range(0, 36):
#     turtle.circle(100, 360)
#     current_heading = turtle.heading()
#     turtle.setheading(current_heading + 10)
#
# screen = t.Screen()
# screen.exitonclick()
