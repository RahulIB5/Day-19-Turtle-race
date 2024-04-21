from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Bet on Turtle", prompt="Which color turtle wins? ")
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
y_axis = int(-120)
all_turtles = []
is_race_on = False

for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[n])
    new_turtle.goto(x=-250, y=y_axis)
    y_axis += 50
    # instead can make list of yaxis distances and add according to index in loop
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 280:
            # 300-(40/2)=280
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"{winning_color} won the bet for you!!!")
            else:
                print(f"{winning_color} is the winner you loose")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
