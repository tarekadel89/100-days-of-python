import os
from supporting_data import MENU, COINS

resources = {
    "water": {"volume": 300, "uom": "ml"},
    "milk": {"volume": 200, "uom": "ml"},
    "coffee": {"volume": 100, "uom": "g"},
}

money = {
    "value": 0,
}


def setup_screen():
    if os.name == 'nt':  # Check if the system is Windows
        os.system('cls')  # Use cls command on Windows
    else:
        os.system('clear')  # Use clear command on other systems
    print("☕️ Welcome to the Coffee Machine ���️")
    

def print_report():
    for resource, data in resources.items():
        print(f"{resource}: {data['volume']}{data['uom']}")
    print(f"Money: ${money['value']}")
    
def check_resources(order):
    lacking_resources = []
    for item, quantity in order.items():
        if item not in resources or resources[item]["volume"] < quantity:
            lacking_resources.append(item)

    if lacking_resources:
        print(f"Sorry there is not enough: {', '.join(lacking_resources)}.")
        return False
    return True

def process_money():
    sum = 0
    for coin in COINS:
        quantity = input(f"How many {coin} coins do you have? ")
        while not quantity.isdigit() or int(quantity) < 0:
            print("Invalid input. Please enter a valid number of coins.")
            quantity = input(f"How many {coin} do you have? ")
        sum += int(quantity) * COINS[coin]
    return sum

def process_payment(payment, price):
    if payment >= price:
        change = payment - price
        print(f"Price is {price}, you paid {payment}, your change is ${change}.")
        money['value'] += price
        return True
    print(f"Insufficient funds. Price is {price}, you paid {payment}.")
    return False

def make_drink(order):
    for ingredient, quantity in order.items():
        resources[ingredient]["volume"] -= quantity
    print("Please, enjoy your drink! :)")
    return True

setup_screen()
user_input = ""
while user_input!= "exit":
    user_input = input("Enter your order (espresso, latte, cappuccino, report, or exit): ").lower()
    while user_input not in ["espresso", "latte", "cappuccino", "report", "exit"]:
        print("Invalid input. Please enter a valid order or 'exit'.")
        user_input = input("Enter your order (espresso, latte, cappuccino, report, or exit): ").lower()
    if user_input == "report":    
        print_report()
    elif user_input in ["espresso", "latte", "cappuccino"]:
        check_resources_result = check_resources(MENU[user_input]["ingredients"])
        if check_resources_result:
            process_payment_result = process_payment(process_money(), MENU[user_input]["cost"])
            if process_payment_result:
                make_drink(MENU[user_input]["ingredients"])