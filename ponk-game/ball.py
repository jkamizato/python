from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(20)
        self.penup()
        self.shape("circle")
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_direction
        new_x = self.xcor() + self.x_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_direction *= -1

    def bounce_x(self):
        self.x_direction *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()
