from flask import Flask
import random

# Generate a random number between 0 and 9

random_number = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Guess, number between 0 and 9!</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
            
@app.route("/guess/<guess>")
def guess(guess):
    global random_number
    if int(guess) == random_number:
        random_number = random.randint(0, 9)
        return "Congratulations! You guessed correctly. Guess again!"
    elif int(guess) > random_number:
        return f"Too high!! "
    else:
        return f"Too low!"      

if __name__ == "__main__":
    app.run(debug=True)
