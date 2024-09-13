import random
from hangman_stages import hangman_stages
from hangman_words import fruits, countries, animals

num_guesses = 0
player_guess = []
guessed_letters = []


def initial_setup(mode):
    """
    This function initializes the game by setting up the necessary variables and choosing a random word from the list of fruits.

    Parameters:
    None

    Returns:
    str: The randomly chosen word from the list of fruits.
    """
    global num_guesses
    global player_guess
    global guessed_letters

    num_guesses = 0
    player_guess = []
    guessed_letters = []
    if mode == "f":
        random_word = random.choice(fruits)
    elif mode == "c":
        random_word = random.choice(countries)
    else:
        random_word = random.choice(animals)
    print(hangman_stages[0])
    for c in random_word:
        player_guess.append("-")
    print("".join(player_guess))
    return random_word

    
def make_guess(word):
    """
    This function handles the player's guess in the Hangman game. It validates the input, checks if the guessed letter
    is already guessed, updates the player's guess, and prints the current state of the game.

    Parameters:
    word (str): The randomly chosen word from the list of fruits.

    Returns:
    None
    """
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
    elif guess.lower() in word or guess.upper() in word:
        print(f"Correct! Attempts left {6-num_guesses}")
        for index in range (len(word)):
            if guess.lower() == word[index].lower():
                player_guess[index] = word[index]
    else:
        num_guesses += 1
        guessed_letters.append(guess)
        print(f"Incorrect! Attempts left {6-num_guesses}")
    print(hangman_stages[num_guesses])
    print("".join(player_guess))


def game_logic():
    """
    This function orchestrates the main game logic of the Hangman game. It initializes the game,
    handles player guesses, and determines the outcome of the game.

    Parameters:
    None

    Returns:
    None
    """
    game_mode = input("Do you want to play with fruits (f), countries (c), or animals (a)? ").lower()
    while game_mode not in ['f', 'c', 'a']:
        print("Invalid input. Please enter f, c, or a")
        game_mode = input("Do you want to play with fruits (f), countries (c), or animals (a)? ").lower()
    computer_word = initial_setup(game_mode)  # Initialize the game by choosing a random word and setting up the necessary variables.
    while num_guesses < 6 and "-" in player_guess:  # Continue the game until the player has made 6 incorrect guesses or has guessed the word correctly.
        make_guess(computer_word)  # Handle the player's guess.
    if num_guesses == 6:  # If the player has made 6 incorrect guesses, they have lost the game.
        print(f"You have failed. The word was {computer_word}")
    else:  # If the player has guessed the word correctly, they have won the game.
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
    
    