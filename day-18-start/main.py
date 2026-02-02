import random
from turtle import Turtle, Screen, colormode


t = Turtle()
screen = Screen()

t.shape("turtle")

# t.color("red")
# for _ in range(10):
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.forward(10)
#

colormode(255)
# t.pensize(15)


def random_walk():
    direction = random.choice([0, 90, 180, 270])
    t.left(direction)
    t.setheading(direction)


def draw_shape(side_shape):
    angle = 360 / side_shape
    for step in range(side_shape):
        t.forward(100)
        t.left(angle)

# for side in range(3, 11):
#     t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     # draw_shape(side)
#     random_walk()

t.speed("fastest")
# for i in range(360):
#     t.circle(100)
#     t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     t.setheading(i)

# for _ in range(100):
#     t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     random_walk()
#     t.forward(30)

t.up()
t.pensize(10)
t.setposition(-300, -300)

row = -300
col = -300
step = 50

def print_dot(move_step):
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.dot()
    t.penup()
    t.forward(move_step)
    t.pendown()

def print_row(move_step):
    times = int(600 / move_step)
    for i in range (0, times):
        print_dot(move_step)

while col <= 300:
    print_row(step)
    col += step
    t.penup()
    t.setposition(-300, col)
    t.pendown()




# step = 50
# while row < 300:
#     while col < 300:
#         print_dot(step)
#         col += step

screen.exitonclick()