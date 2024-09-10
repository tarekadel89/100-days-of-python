import random

options = ["heads", "tails"]

def coin_flip():
    return random.choice(options)

print (coin_flip())