from turtle import Turtle

FONT = ("Arial", 16, "normal")
ALIGNMENT = "center"
BOUNDARY = 280

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, BOUNDARY)
        self.pencolor("white")
        self.refresh()
        self.hideturtle()

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.refresh()

    """def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align=ALIGNMENT, font=FONT)"""