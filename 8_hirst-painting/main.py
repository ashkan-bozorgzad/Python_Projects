from Extract_color import rgb_colors
import turtle as t
import random

color_list = rgb_colors[5:]

tim = t.Turtle()

t.colormode(255)
tim.speed(0)
tim.penup()
tim.goto(-315, -315)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(70)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(70)
        tim.setheading(180)
        tim.forward(700)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
