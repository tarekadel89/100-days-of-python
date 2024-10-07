#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invitees = []
with open("Day 024/Input/Names/invited_names.txt", "r") as file:
    invitees = [line.strip() for line in file.readlines()]

with open("Day 024/Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()

for name in invitees:
    new_letter = starting_letter.replace("[name]", name)
    with open(f"Day 024/Output/ReadyToSend/{name}_invite_letter.txt", "w") as file:
        file.write(new_letter)