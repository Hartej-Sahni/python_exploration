from turtle import Turtle

BOUNDARY = 290

class Snake:
    def __init__(self):
        self.snake_blocks = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        for i in range(0, 3):
            new_block = self.create_block()
            new_block.goto(x, y)
            self.snake_blocks.append(new_block)
            x -= 20

    def move(self):
        for block in range(len(self.snake_blocks) - 1, 0, -1):
            x_new = self.snake_blocks[block - 1].xcor()
            y_new = self.snake_blocks[block - 1].ycor()
            self.snake_blocks[block].goto(x_new, y_new)
        self.snake_blocks[0].forward(20)

    def up(self):
        if self.snake_blocks[0].heading() != 270:
            self.snake_blocks[0].setheading(90)

    def down(self):
        if self.snake_blocks[0].heading() != 90:
            self.snake_blocks[0].setheading(270)

    def left(self):
        if self.snake_blocks[0].heading() != 0:
            self.snake_blocks[0].setheading(180)

    def right(self):
        if self.snake_blocks[0].heading() != 180:
            self.snake_blocks[0].setheading(0)

    def create_block(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        return t

    def extend(self):
        new_block = self.create_block()
        x = self.snake_blocks[-1].xcor()
        y = self.snake_blocks[-1].ycor()
        new_block.goto(x, y)
        self.snake_blocks.append(new_block)

    def hit_wall(self):
        if self.snake_blocks[0].xcor() > BOUNDARY or self.snake_blocks[0].xcor() < -1 * BOUNDARY \
                or self.snake_blocks[0].ycor() > BOUNDARY or self.snake_blocks[0].ycor() < -1 * BOUNDARY:
            return True
        return False

    def hit_tail(self):
        for block in self.snake_blocks[1:]:
            if self.snake_blocks[0].distance(block) < 15:
                return True
        return False

    def reset(self):
        for block in self.snake_blocks:
            block.goto(1000, 1000)
        self.snake_blocks.clear()
        self.create_snake()
        print(self.snake_blocks)

