from turtle import  Screen , Turtle
import time
from scoreboard import Scoreboard
from snake import Snake 
from food import Food
border_turtle = Turtle()
border_turtle.speed(0)
border_turtle.color("white")
border_turtle.pensize(5)
border_turtle.hideturtle()

def draw_border():
  border_turtle.penup()
  border_turtle.goto(-300,300)
  border_turtle.pendown()
  for _ in range(4):
    border_turtle.forward(600)
    border_turtle.right(90)

draw_border()

#Screen setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
   #detect collisioon with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score_board.increase_score()

  
  #detect collision with wall
  if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
    game_is_on = False
    score_board.reset()  

  #collision with tail
  for segment in snake.snake_body[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      score_board.reset()

screen.exitonclick()