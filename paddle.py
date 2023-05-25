from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(position)

    def move_up(self):
        y_pos = self.ycor() + 20
        self.sety(y_pos)

    def move_down(self):
        y_pos = self.ycor() - 20
        self.sety(y_pos)
