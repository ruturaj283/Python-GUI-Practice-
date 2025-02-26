from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("snake game/data.txt") as data:
      self.high_score = int(data.read())

    self.color("white")
    self.penup()
    self.goto(0,265)
    self.hideturtle()
    self.update_scoreboard()

  
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score:{self.high_score}", align =ALIGNMENT, font = FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("snake game/data.txt",mode = 'w') as data:
        data.write(f"{self.high_score}")
    self.score = 0
    self.update_scoreboard()
  
  # def gameover(self):
  #   self.goto(0,0)
  #   self.write("GAME OVER", align =ALIGNMENT, font = FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

    