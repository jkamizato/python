import random
from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -150
turtles = []
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    y_position += 50
    tim.goto(x=-230,y=y_position)
    turtles.append(tim)

keep_running = True

while keep_running:
    for turtle in turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 230:
            keep_running = False
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print(f"You lost! The turtle {turtle.pencolor()} wins!")

screen.exitonclick()