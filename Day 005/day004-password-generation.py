import random

special_characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~"]
password = []

def generate_letters():
    """
    This function generates a specified number of random letters, both uppercase and lowercase,
    and appends them to the global 'password' list.

    Parameters:
    None

    Returns:
    None

    Note:
    The function prompts the user to input the number of letters required for the password.
    It validates the input to ensure it is a positive integer.
    The generated letters are appended to the global 'password' list.
    """
    letters_length = input("How many letters should the password contain? ")
    while not letters_length.isdigit() or int(letters_length) <= 0:
        print("Invalid input. Please enter a positive integer.")
        letters_length = input("How many letters should the password contain? ")

    for _ in range(int(letters_length)):
        letter = chr(random.randint(ord('a'), ord('z')))
        uppercase = random.randint(0, 1)
        if uppercase == 1:
            letter = letter.upper()
        password.append(letter)

def generate_symbols():
    """
    This function generates a specified number of random special characters,
    and insert them in random indices to the global 'password' list.

    Parameters:
    None

    Returns:
    None

    Note:
    The function prompts the user to input the number of special characters required for the password.
    It validates the input to ensure it is a positive integer.
    The generated symbols are inserted randomly to the global 'password' list.
    """
    symbols_length = input("How many symbols should the password contain? ")
    while not symbols_length.isdigit() or int(symbols_length) <= 0:
        print("Invalid input. Please enter a positive integer.")
        symbols_length = input("How many symbols should the password contain? ")
    
    for _ in range(int(symbols_length)):
        symbol = random.choice(special_characters)
        index = random.randint(0, len(password) - 1)
        password.insert(index, symbol)

def generate_digits():
    """
    This function generates a specified number of random digits,
    and insert them in random indices to the global 'password' list.

    Parameters:
    None

    Returns:
    None

    Note:
    The function prompts the user to input the number of digits required for the password.
    It validates the input to ensure it is a positive integer.
    The generated digits are inserted randomly to the global 'password' list.
    """
    digits_length = input("How many digits should the password contain? ")
    while not digits_length.isdigit() or int(digits_length) <= 0:
        print("Invalid input. Please enter a positive integer.")
        digits_length = input("How many digits should the password contain? ")
    
    for _ in range(int(digits_length)):
        digit = str(random.randint(0, 9))
        index = random.randint(0, len(password) - 1)
        password.insert(index, digit)
            
generate_letters()
generate_symbols()
generate_digits()
print("".join(password))