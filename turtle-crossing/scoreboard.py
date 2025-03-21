from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align="center", font=FONT)