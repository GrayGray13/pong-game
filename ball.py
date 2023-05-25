from turtle import Turtle

STARTING_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x_move = STARTING_SPEED
        self.y_move = STARTING_SPEED

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.setpos(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.setpos(0, 0)
        self.bounce_x()