from art import logo, vs
from game_data import data
import os
import random

def setup_screen():
    """
    This function clears the terminal screen and prints the ASCII art logo.

    Parameters:
    None

    Returns:
    None
    """
    if os.name == 'nt':  # Check if the system is Windows
        os.system('cls')  # Use cls command on Windows
    else:
        os.system('clear')  # Use clear command on other systems
    print(logo)


def generate_round(first_account, selectedAccounts):
    """
    This function generates a new round for the game by selecting two unique accounts from the data list.
    If the first account is None, it randomly selects an account that has not been selected before.
    Then, it randomly selects a second account that has not been selected before.

    Parameters:
    first_account (str): The first account selected for the round. If None, a new account will be randomly selected.
    selectedAccounts (list): A list of accounts that have already been selected in previous rounds.

    Returns:
    tuple: A tuple containing the two selected accounts for the round.
    """
    if first_account == "None":
        first_account = random.choice(data)
        while first_account in selectedAccounts:
                first_account = random.choice(data)
        selectedAccounts.append(first_account)
    second_account = random.choice(data)
    while second_account in selectedAccounts:
            second_account = random.choice(data)
    selectedAccounts.append(first_account)
    return first_account, second_account, selectedAccounts

    
def check_answer(fAccount, sAccount, user_choice, currentScore):
    """
    This function checks the user's answer for the current round and updates the score accordingly.

    Parameters:
    fAccount (dict): A dictionary representing the first account selected for the round.
    sAccount (dict): A dictionary representing the second account selected for the round.
    user_choice (str): The user's choice for which account has more followers ('A' or 'B').
    currentScore (int): The current score of the user.

    Returns:
    tuple: A tuple containing a boolean indicating whether the round is still ongoing (True) or the game is over (False),
           and the updated score.
    """
    setup_screen()
    if (user_choice == 'A' and fAccount['follower_count'] > sAccount['follower_count']) or (user_choice == 'B' and fAccount['follower_count'] < sAccount['follower_count']): 
        currentScore += 1
        print(f"You're right! Current score: {currentScore}")
        return True, currentScore
    print(f"Wrong! Final score: {currentScore}")
    return False, currentScore

def keep_playing():
    """
    This function prompts the user to decide whether to play again or not.
    It keeps asking for input until the user enters a valid choice ('Y' or 'N').
    If the user chooses to play again, it returns True. Otherwise, it returns False.

    Parameters:
    None

    Returns:
    bool: True if the user wants to play again, False otherwise.
    """
    user_choice = input("Do you want to play again? (Y/N): ").upper()
    while user_choice not in ['Y', 'N']:
        print("Invalid choice. Please, type 'Y' or 'N'")
        user_choice = input("Do you want to play again? (Y/N): ").upper()
    if user_choice == 'Y':
        return True
    else:
        return False


def game_logic():
    """
    This function orchestrates the game logic, including setting up the screen, generating rounds,
    displaying account information, accepting user input, checking answers, and keeping track of the score.

    Parameters:
    None

    Returns:
    None
    """
    setup_screen()
    nextRound = True
    selectedAccounts = []
    fAccount = "None"
    sAccount = "None"
    score = 0

    while(nextRound):
        fAccount, sAccount, selectedAccounts = generate_round(fAccount, selectedAccounts)
        print(f"Compare A: {fAccount['name']}, {fAccount['description']} from {fAccount['country']}")
        print(vs)
        print(f"Compare B: {sAccount['name']}, {sAccount['description']} from {sAccount['country']}")
        user_choice = input("Who has more followers? (A/B): ").upper()
        while user_choice not in ['A', 'B']:
            print("Invalid input. Please enter A or B.")
            user_choice = input("Who has more followers? (A/B): ").upper()
        nextRound, score = check_answer(fAccount, sAccount, user_choice, score)
        if nextRound and user_choice == 'B':
            fAccount = sAccount
        if nextRound:
            nextRound = keep_playing()



new_game = "Y"
while new_game == "Y":
    game_logic()
    new_game = input("Do you want to start a new game? (Y/N): ").upper()
    while new_game not in ['Y', 'N']:
        print("Invalid choice. Please, type 'Y' or 'n'")
        new_game = input("Do you want to start a new game? (Y/N): ").upper()