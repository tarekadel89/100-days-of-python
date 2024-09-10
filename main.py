import random

options = ["rock", "paper", "scissors"]

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  return {"player": player_choice, "computer": random.choice(options)}

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock": 
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    elif computer == "paper":
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    elif computer == "scissors":
      return "Scissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    elif computer == "rock":
      return "Rock smashes scissors! You lose."

choices = get_choices()
print(check_win(choices["player"], choices["computer"]))

