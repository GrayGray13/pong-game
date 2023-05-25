from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
time_interval = 0.06
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

while game_is_on:
    time.sleep(time_interval)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        if time_interval != 0.0:
            time_interval -= 0.01

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        time_interval = 0.06

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        time_interval = 0.06

screen.exitonclick()
