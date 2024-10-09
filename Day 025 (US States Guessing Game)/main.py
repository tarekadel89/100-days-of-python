import pandas as pd
import turtle as t

my_screen = t.Screen()
my_screen.bgpic("Day 025 (US States Guessing Game)/blank_states_img.gif")
my_screen.title("U.S. States Guessing Game")

data = pd.read_csv("Day 025 (US States Guessing Game)/50_states.csv")
all_states = data["state"].tolist()

user_input = "none"
guessed_states = []

while user_input.lower() != "Exit" or len(guessed_states) == 50: 
    try:
        user_input = my_screen.textinput(f"{len(guessed_states)}/50 guessed", "Enter a state name or 'exit': ").title()
        if user_input.lower() == "exit":
            break
        if user_input in all_states and user_input not in guessed_states:
            guessed_states.append(user_input)
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

ungessed_states = [state for state in all_states if state not in guessed_states]
df = pd.DataFrame(ungessed_states, columns=["Ungessed States"])
df.to_csv("Day 025 (US States Guessing Game)/unsolved_states.csv", index=False)