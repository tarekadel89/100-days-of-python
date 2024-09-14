import os

def make_bid():
    """
    This function prompts the user to enter their name and bid for an auction.
    It validates the name to ensure it only contains alphabetic characters and
    the bid to ensure it is a positive decimal number.

    Parameters:
    None

    Returns:
    tuple: A tuple containing the user's name (as a string) and their bid (as a float).
    """
    name = input("Enter your name: ").title()
    while not name.isalpha():
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ").title()
    bid = input("Enter your bid: $")
    while not bid.replace('.', '', 1).isdigit() or float(bid) <= 0:
        print("Invalid bid. Please enter a valid positive amount.")
        bid = input("Enter your bid: $")
    bid = float(bid)
    return name, bid


def decide_winner(final_bids):
    """
    This function determines the winner of an auction based on the final bids.
    If no bids are received, it prints a message indicating no winner.
    Otherwise, it finds the bidder with the highest bid and prints their name and bid amount.

    Parameters:
    final_bids (dict): A dictionary where keys are bidder names (strings) and values are bid amounts (floats).

    Returns:
    bool: Always returns True.
    """
    if len(final_bids) == 0:
        print("No bids received. No winner.")
    else:
        winner = max(final_bids, key=final_bids.get)  # Find the name with the highest bid
        print(f"Winner is {winner} with a bid of ${final_bids[winner]:.2f}.")
    return True



def play_game():
    """
    This function orchestrates the bidding game. It collects bids from multiple users,
    validates the uniqueness of bidder names, and determines the winner based on the highest bid.
    It also clears the console screen between rounds for a clean user experience.

    Parameters:
    None

    Returns:
    None
    """
    bids = {}
    more_bidding = True
    while more_bidding:
        name, bid = make_bid()  # Unpack the returned tuple into name and bid variables
        if name not in bids:  # Check if name is not already a key in the bids dictionary
            bids[name] = bid  # Insert the key-value pair into the bids dictionary
        else:
            print(f"A bid from {name} already exists. Please enter a different name.")
        other_bidders = input("Do you have any other bidders? (y/n): ").lower()
        while other_bidders not in ['y', 'n']:
            print("Invalid input. Please enter y or n.")
            other_bidders = input("Do you have any other bidders? (y/n): ").lower()
        if other_bidders == 'n':
            more_bidding = False
        if os.name == 'nt':  # Check if the system is Windows
            os.system('cls')  # Use cls command on Windows
        else:
            os.system('clear')  # Use clear command on other systems
    decide_winner(bids)


print("Welcome to the Bidding Game!")
play_game()