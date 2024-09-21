from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

def setup_screen():
    if os.name == 'nt':  # Check if the system is Windows
        os.system('cls')  # Use cls command on Windows
    else:
        os.system('clear')  # Use clear command on other systems
    print("☕️ Welcome to the Coffee Machine ���️")

setup_screen()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

user_input = ""

while user_input!= "off":
    user_input = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    while user_input not in my_menu.get_items() and user_input not in ["report", "off"]:
        print("Invalid input. Please enter a valid option or 'report' or 'off'.")
        user_input = input(f"What would you like? ({my_menu.get_items()}): ").lower()
        
    if user_input == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif user_input in my_menu.get_items():
        selected_item = my_menu.find_drink(user_input)
        is_resource_sufficient_result = my_coffee_maker.is_resource_sufficient(selected_item)
        if is_resource_sufficient_result:
            payment_result = my_money_machine.make_payment(selected_item.cost)
            if payment_result:
                my_coffee_maker.make_coffee(selected_item)  