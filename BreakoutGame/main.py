import turtle
import math

BAR_STEP = 20

window = turtle.Screen()
window.setup(0.5, 0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("Breaker Block")
window.setup(width=800, height=600)
window.tracer(0)


def move_left():
    x = paddle.xcor()
    if x > -330:
        paddle.setx(paddle.xcor() - BAR_STEP)

def move_right():
    x = paddle.xcor()
    if x < 330:
        paddle.setx(paddle.xcor() + BAR_STEP)

# Paddle
paddle = turtle.Turtle('square')
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.sety(-250)

# Ball
ball = turtle.Turtle("circle")
ball.color("red")
ball.speed(0)
ball.pensize(1)
ball.penup()
ball.dx = 0.5
ball.dy = 0.5
radio = math.sqrt(2)*0.5

# Bricks
bricks = []
colors = ["red", "orange", "green", "blue"]

# Create rows of bricks
for y in range(150, 250, 30):
    for x in range(-350, 400, 70):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[(y-150)//30 % len(colors)])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

## Movement
window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# 7. Main Game Loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall Collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle Collision
    if -250 < ball.ycor() < -230:
        # 0.
        new_x = (((ball.xcor() - paddle.xcor()) / 60) * 0.9) * radio
        new_y = (math.sqrt(1 - (new_x * new_x))) * radio
        result = math.sqrt(new_x * new_x + new_y * new_y)
        # Y invert
        if paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60:
            ball.dy = new_y
            ball.dx = new_x

    # Brick Collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.hideturtle() # Hide brick
            bricks.remove(brick) # Remove from list
            ball.dy *= -1
            break # Avoid multiple collisions in one frame

    # Game Over
    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball.dy *= -1