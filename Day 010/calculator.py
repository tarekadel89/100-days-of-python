import os
from operations_definition import operations

def calc_step(carry_over):
    """
    This function performs a basic arithmetic operation on two numbers.
    If a carry_over value is provided, it will be used as the first number in the operation.
    Otherwise, the user will be prompted to enter the first number.
    The user will then be prompted to enter an operation (+, -, *, /).
    If the operation is invalid, the user will be prompted again.
    The user will then be prompted to enter the second number.
    If the second number is invalid, the user will be prompted again.
    The result of the operation will be printed, and the function will return the result.

    Parameters:
    carry_over (str): The first number for the operation. If "None", the user will be prompted to enter a number.

    Returns:
    float: The result of the arithmetic operation.
    """
    if carry_over == "None":
        first_number = input("Enter the first number: ")
        while not first_number.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid number.")
            first_number = input("Enter the first number: ")
    else:
        first_number = carry_over

    operation = input("Enter the operation (+, -, *, /): ")
    while operation not in operations:
        print("Invalid operation. Please enter a valid operation.")
        operation = input("Enter the operation (+, -, *, /): ")

    second_number = input("Enter the second number: ")
    while not second_number.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid number.")
        second_number = input("Enter the second number: ")
    output = operations[operation](float(first_number), float(second_number))
    print(f"Result of {first_number} {operation} {second_number} = {output}")
    return output


exit = False
num1 = "None"
print("Welcome to the Calculator!")
while not exit:
    result = calc_step(num1)
    choice = input("Use the result as an input for another operation [y], new calculation [n], any other key to exit: ").lower()
    if choice == "y":
        num1 = result
    elif choice == "n":
        if os.name == 'nt':  # Check if the system is Windows
            os.system('cls')  # Use cls command on Windows
        else:
            os.system('clear')  # Use clear command on other systems
        print("Fresh start!")
        num1 = "None"
    else:
        exit = True
        print("Goodbye!")
