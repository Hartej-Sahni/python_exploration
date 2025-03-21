import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        num = random.randint(1, 6)
        if num == 1:
            y = random.randint(-230, 230)
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2)
            car.goto(280, y)
            car.setheading(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if (car.xcor() < -280):
                x = random.randint(10, 280)
                car.goto(x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT