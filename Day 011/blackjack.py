import random
import os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def initial_setup():
    """
    This function initializes the game by dealing two cards to the player and the computer.
    It prints the player's hand and the computer's hand with one card hidden.

    Parameters:
    None

    Returns:
    tuple: A tuple containing two lists, representing the player's hand and the computer's hand.
    """
    player_hand = []
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))

    computer_hand = []
    computer_hand.append(random.choice(deck))
    computer_hand.append(random.choice(deck))

    print(f"your hand is {player_hand}")
    print(f"Computer hand is [{computer_hand[0]}, x]")
    return player_hand, computer_hand

    

def calculate_score(hand):
    """
    Calculates the score of a given hand in the game of Blackjack.

    Parameters:
    hand (list): A list of integers representing the cards in the hand. Each card is represented by its value,
                 where 11, 12, 13, and 14 represent Jack, Queen, King, and Ace respectively.

    Returns:
    int: The score of the hand. If the score exceeds 21 and there is an Ace in the hand, the function reduces the Ace's value
         from 11 to 1 until the score is less than or equal to 21.
    """
    total = sum(hand)
    if total > 21:
        for card in hand:
            if card == 11:
                total -= 10
                if total <= 21:
                    break
    return total


def computer_turn(computer_hand, player_score):
    """
    This function simulates the computer's turn in the game of Blackjack.
    The computer will draw cards until its score is 17 or higher, or until it beats the player's score.

    Parameters:
    computer_hand (list): A list of integers representing the cards in the computer's hand.
                          Each card is represented by its value, where 11, 12, 13, and 14 represent
                          Jack, Queen, King, and Ace respectively.
    player_score (int): The score of the player's hand.

    Returns:
    list: The updated computer's hand after drawing cards.
    """
    print(f"Computer initial hand = {computer_hand}")

    while calculate_score(computer_hand) < 17 or calculate_score(computer_hand) < player_score:
        computer_hand.append(random.choice(deck))
        print(f"Computer hand is {computer_hand}")
    return computer_hand


def compare_hands(player_hand, computer_hand):
    """
    Compares the scores of the player's and computer's hands in a game of Blackjack.
    Prints the outcome of the game based on the scores.

    Parameters:
    player_hand (list): A list of integers representing the cards in the player's hand.
                        Each card is represented by its value, where 11, 12, 13, and 14 represent
                        Jack, Queen, King, and Ace respectively.
    computer_hand (list): A list of integers representing the cards in the computer's hand.
                          Each card is represented by its value, where 11, 12, 13, and 14 represent
                          Jack, Queen, King, and Ace respectively.

    Returns:
    None
    """
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    if computer_score > 21:
        print(f"Computer's hand is {computer_hand} - Score: {computer_score} went over 21.. you win!")
    elif player_score > computer_score:
        print(f"Your hand is {player_hand} - Score {player_score}, computer's hand is {computer_hand} - Score {computer_score}. You win!")
    elif player_score < computer_score:
        print(f"Your hand is {player_hand} - Score {player_score}, computer's hand is {computer_hand} - Score {computer_score}. You lose!")
    else:
        print(f"Your hand is {player_hand} - Score {player_score}, computer's hand is {computer_hand} - Score {computer_score}. It's a tie!")

    


def blackjack():
    """
    This function simulates a game of Blackjack. It initializes the game, allows the player to draw cards,
    calculates the scores, and determines the winner based on the rules of Blackjack.

    Parameters:
    None

    Returns:
    None
    """
    player_hand, computer_hand = initial_setup()
    another_card = 'y'

    while another_card == 'y' and calculate_score(player_hand) <= 21:
        another_card = input("Would you like to draw another card [y/n]?: ").lower()
        while another_card not in ['y', 'n']:
            print("Invalid choice. Pease, type 'y' or 'n'")
            another_card = input("Would you like to draw another card [y/n]?: ").lower()
        if another_card == 'y':
            player_hand.append(random.choice(deck))
            print(f"your hand is {player_hand}")

    player_score = calculate_score(player_hand)
    if player_score > 21:
        print(f"Your hand is {player_score} went over 21.. you lost!")
    else:
        computer_hand = computer_turn(computer_hand, player_score)
        compare_hands(player_hand, computer_hand)

if os.name == 'nt':  # Check if the system is Windows
    os.system('cls')  # Use cls command on Windows
else:
    os.system('clear')  # Use clear command on other systems        
print("Welcome to the Blackjack game!")
keep_playing = 'y'
while keep_playing == 'y':
    blackjack()
    keep_playing = input("Do you want to play another round [y/n]?: ").lower()
    while keep_playing not in ['y', 'n']:
        print("Invalid choice. Please, type 'y' or 'n'")
        keep_playing = input("Do you want to play another round [y/n]?: ").lower()
    if os.name == 'nt':  # Check if the system is Windows
        os.system('cls')  # Use cls command on Windows
    else:
        os.system('clear')  # Use clear command on other systems