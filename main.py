from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(30)


def move_backward():
    tim.back(30)


def turn_left():
    tim.left(10)
#   new_heading=tim.heading + 10
#   tim.setheading(new_heading)


def turn_right():
    tim.right(10)
#   new_heading=tim.heading - 10
#   tim.setheading(new_heading)


def clearing():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=clearing, key="c")


screen.exitonclick()
