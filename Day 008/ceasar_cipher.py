alphabet = ["a", "b", "c", "d", "e", "f", "g", 
            "h", "i", "j", "k", "l", "m", "n", 
            "o", "p", "q", "r", "s", "t", "u", 
            "v", "w", "x", "y", "z"]

""" def encode_string(str, shift):
    global alphabet
    encoded_string = ""
    for char in str:
        if char.lower() not in alphabet:
           encoded_string += char
        else:
            index = alphabet.index(char.lower())
            encoded_index = (index + shift) % 26
            if char.isupper():
                encoded_string += alphabet[encoded_index].upper()
            else:
                encoded_string += alphabet[encoded_index]
    return encoded_string

def decode_string(str, shift):
    global alphabet
    decoded_string = ""
    for char in str:
        if char.lower() not in alphabet:
            decoded_string += char
        else:
            index = alphabet.index(char.lower())
            decoded_index = (index - shift) % 26
            if char.isupper():
                decoded_string += alphabet[decoded_index].upper()
            else:
                decoded_string += alphabet[decoded_index]
    return decoded_string """

def encode_decode(mode, str, shift):
    """
    This function performs a Caesar cipher encoding or decoding on a given string.

    Parameters:
    mode (str): The mode of operation. It should be either 'encode' or 'decode'.
    str (str): The input string to be encoded or decoded.
    shift (int): The number of positions to shift each letter in the alphabet.

    Returns:
    str: The encoded or decoded string.
    """
    global alphabet
    output_str = ""
    for char in str:
        if char.lower() not in alphabet:
            output_str += char
        else:
            index = alphabet.index(char.lower())
            if mode == "encode":
                output_str += alphabet[(index + shift) % 26].upper() if char.isupper() else alphabet[(index + shift) % 26]
            else:
                output_str += alphabet[(index - shift) % 26].upper() if char.isupper() else alphabet[(index - shift) % 26]
    return output_str


mode_input = input("Enter 'encode' or 'decode': ").lower()
while mode_input not in ["encode", "decode"]:
    print("Invalid mode. Please enter 'encode' or 'decode'.")
    mode_input = input("Enter 'encode' or 'decode': ").lower()
    
str_input = input(f"Enter the string to {mode_input}: ")

shift_input = input("Enter the shift value: ")
while not shift_input.isdigit() or int(shift_input) < 1:
    print("Invalid input. Please enter a positive integer.")
    shift_input = input("Enter the shift value: ")
    
print(f"{mode_input}ed string: {encode_decode(mode_input, str_input, int(shift_input))}")
