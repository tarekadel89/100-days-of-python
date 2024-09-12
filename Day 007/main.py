import random
from hangman_stages import hangman_stages
from hangman_words import fruits

num_guesses = 0
player_guess = []
guessed_letters = []


def initial_setup():
    global num_guesses
    global player_guess
    global guessed_letters
    
    num_guesses = 0
    player_guess = []
    guessed_letters = []
    random_word = random.choice(fruits)
    print(hangman_stages[0])
    for c in random_word:
        player_guess.append("-")
    print("".join(player_guess))
    print(random_word)
    return random_word
    
def make_guess(word):
    global num_guesses
    global player_guess
    global guessed_letters
    
    guess = input("Guess a letter: ").lower()
    while guess not in "abcdefghijklmnopqrstuvwxyz" and len(guess) > 0:
        print("Please enter a lowercase letter.")
        guess = input("Guess a letter: ").lower()
    
    if guess in player_guess:
        print("You've already guessed that letter successfully!")
    elif guess in guessed_letters:
        print("You've already guessed that letter and it's not in the word")
    elif guess in word:
        print(f"Correct! Attempts left {6-num_guesses}")
        index = 0
        for c in word:
            if guess == c:
                player_guess[index] = guess
            index += 1
    else:
        num_guesses += 1
        guessed_letters.append(guess)
        print(f"Incorrect! Attempts left {6-num_guesses}")
    print(hangman_stages[num_guesses])
    print("".join(player_guess))  

def game_logic():
    computer_word = initial_setup()
    while num_guesses < 6 and "-" in player_guess:
        make_guess(computer_word)
    if num_guesses == 6:
        print(f"You have failed. The word was {computer_word}")
    else:
        print("You have guesssed it correctly")


print("Welcome to Hangman!")
print("Guess the name of a fruit in 6 attempts")
keep_playing = True
while keep_playing:
    game_logic()
    user_choice = input("Do you want to keep playing (y/n): ").lower()
    if user_choice != "y":
        keep_playing = False
        print("Ok, goodbye! Come back later!")
    else:
        print("Yay, let's do another round!")
    
    