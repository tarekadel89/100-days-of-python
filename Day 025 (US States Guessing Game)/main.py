import pandas as pd
import turtle as t

my_screen = t.Screen()
my_screen.bgpic("Day 025 (US States Guessing Game)/blank_states_img.gif")
my_screen.title("U.S. States Guessing Game")

data = pd.read_csv("Day 025 (US States Guessing Game)/50_states.csv")
all_states = data["state"].tolist()

user_input = "none"
count = 0
while user_input.lower() != "exit" or count == 50: 
    try:
        user_input = my_screen.textinput(f"{count}/50 guessed", "Enter a state name or 'exit': ").title()
        if user_input.lower() == "exit":
            break
        if user_input in all_states:
            count += 1
            row = data[data["state"] == user_input]
            x = row["x"].values[0]
            y = row["y"].values[0]
            state = t.Turtle()
            state.hideturtle()
            state.penup()
            state.teleport(x, y)
            state.write(user_input, align="center", font=("Arial", 8, "normal"))
    except:
        break