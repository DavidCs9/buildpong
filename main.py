from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)


user_1 = Paddle(0)
user_2 = Paddle(1)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(user_1.move_paddle_up, "w")
screen.onkeypress(user_2.move_paddle_up, "Up")
screen.onkeypress(user_1.move_paddle_down, "s")
screen.onkeypress(user_2.move_paddle_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    # detect collition with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collition with the paddles
    if ball.distance(user_1) < 50 and ball.xcor() < -350 or ball.distance(user_2) < 50 and ball.xcor() > 350:
        ball.bounce_x()

    # detect collition with the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()


    # detect collition with the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()





screen.exitonclick()
