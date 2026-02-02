from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    t = Turtle("square")
    t.penup()
    t.pensize(20)
    t.color("white")
    t.goto(position)
    segments.append(t)


game_is_on = True


screen.exitonclick()