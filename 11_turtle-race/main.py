from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=396)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a colour: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple", ]
y_positions = [166, 100, 34, -32, -98, -164]
should_continue = False
all_turtles = []

for turtle_index in range(0, 6):
    new_segment = Turtle(shape="turtle")
    new_segment.penup()
    new_segment.color(colors[turtle_index])
    new_segment.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_segment)

if user_bet:
    should_continue = True

while should_continue:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            should_continue = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} is the winner turtle.")
            else:
                print(f"You've lost. The {winning_color} is the winner turtle.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
