from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        if not self.hit_top():
            self.forward(MOVE_DISTANCE)

    def hit_top(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def reset(self):
        self.goto(STARTING_POSITION)
