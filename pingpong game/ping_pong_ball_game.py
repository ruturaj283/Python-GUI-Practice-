from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from ball_scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(
    0
)  #stops animation on objects but needs manual update so that objects show on screen
# BALL
ball = Ball()
#Scoreboard
scoreboard = Scoreboard()
#PADDLE
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #detect collision
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # detection collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
  #paddle misses ball
  if ball.xcor() > 380:#r_paddle misses
    ball.reset_position()
    scoreboard.l_point()
  if ball.xcor() < -380:#l_paddle misses
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()
