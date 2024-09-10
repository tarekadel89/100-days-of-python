import random

options = ["rock", "paper", "scissors"]


def get_player_choice():
    """
    This function prompts the user to enter a choice (rock, paper, or scissors) and validates the input.
    If the input is invalid, it keeps asking until a valid choice is entered.

    Parameters:
    None

    Returns:
    str: The validated player's choice (rock, paper, or scissors).
    """
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    while player_choice.lower() not in options:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player_choice = input("Enter a choice (rock, paper, scissors): ")
    return player_choice.lower()

        
def get_computer_choice():
    """
    This function generates a random choice for the computer player.

    Parameters:
    None

    Returns:
    str: The computer's choice (rock, paper, or scissors). The choice is randomly selected from the 'options' list.
    """
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
    print(f"You chose {player_choice}, computer chose {computer_choice}")
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

keep_playing = True    
while keep_playing:
    print(determine_winner(get_player_choice(), get_computer_choice()))
    another_round = input("Do you want to play again? (yes/no): ").lower()
    if another_round != "yes":
        keep_playing = False