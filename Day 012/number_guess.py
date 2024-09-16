import os
import random
from art import logo
from difficulties import difficulty_levels

def initial_setup():
    print("Choose your difficulty level")
    for key, value in difficulty_levels.items():
        print(f"{key}, {value} attempts.")
    chosen_difficulty = input("Enter your choice (easy/medium/hard): ").lower()
    while chosen_difficulty not in difficulty_levels:
        print("Invalid difficulty level. Please choose from easy, medium, or hard.")
        chosen_difficulty = input("Enter your choice (easy/medium/hard): ").lower()
    return difficulty_levels[chosen_difficulty]

def play_game():
    attempts = initial_setup() # Initialize
    number_to_guess = random.randint(1, 100)
    guess = 0

    while attempts > 0 and guess!= number_to_guess:
        print(f"You have {attempts} attempts left.")
        guess = input("Guess a number between 1 and 100: ")
        while not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("Invalid input. Please enter a valid number between 1 and 100.")
            guess = input("Guess a number between 1 and 100: ")
        guess = int(guess)
        if guess == number_to_guess:
            print("Congratulations! You guessed the number correctly.")
        else:
            attempts -= 1
            if guess < number_to_guess:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The number was {number_to_guess}.")

keep_playing = 'y'
while keep_playing == 'y':
    if os.name == 'nt':  # Check if the system is Windows
        os.system('cls')  # Use cls command on Windows
    else:
        os.system('clear')  # Use clear command on other systems        
    print (logo)
    play_game()
    keep_playing = input("Do you want to play again? (y/n): ").lower()
    while keep_playing not in ['y', 'n']:
        print("Invalid input. Please enter y or n.")
        keep_playing = input("Do you want to play again? (y/n): ").lower()
    