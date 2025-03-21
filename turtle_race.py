from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle do you bet will win a race? Enter a color: ").lower()
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -150
turtles = []
for color in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.color(color)
    t.goto(x, y)
    turtles.append(t)
    y += 50

winner_color = ""
race_over = False
while not race_over:
    for turtle in turtles:
        distance = random.randint(0, 20)
        turtle.forward(distance)
        pos = turtle.position()
        if pos[0] >= 250:
            winner_color = turtle.pencolor()
            print(f"The winning turtle is {winner_color}.")
            race_over = True
            break

if (user_bet == winner_color):
    print("You won the bet!")
else:
    print("You lost the bet.")


screen.exitonclick()