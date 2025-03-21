from turtle import Turtle, Screen, shape
import pandas

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

states_df = pandas.read_csv("50_states.csv")
all_states = states_df["state"].tolist()
score = 0
states_entered = []
while len(states_entered) < 50:
    user_state = screen.textinput(title=f"Score: {score}/50", prompt="Enter a state: ").title()
    print(user_state)
    if (user_state == "Exit"):
        break
    if len(states_df[states_df["state"] == user_state]) == 1 and user_state not in states_entered:
        states_entered.append(user_state)
        score += 1
        state_xcoor = states_df[states_df["state"] == user_state]["x"].tolist()[0]
        state_ycoor = states_df[states_df["state"] == user_state]["y"].tolist()[0]
        t = Turtle()
        t.penup()
        t.goto(state_xcoor, state_ycoor)
        t.write(f"{user_state}")
        t.hideturtle()

missing_states = list(set(all_states) - set(states_entered))
dict_missing_states = {
    "States": missing_states
}
missing_df = pandas.DataFrame(dict_missing_states)
missing_df.to_csv("missing_states.csv")