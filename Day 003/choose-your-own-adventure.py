print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

direction = input("Choose a direction (right or left): ").lower()
while direction != "right" and direction != "left":
    print("Invalid direction. Please choose either 'right' or 'left'.")
    direction = input("Choose a direction (right or left): ").lower()
if direction == "left":
    print("Wrong choice! Game Over!")
    exit()

method = input("Choose a method (swim or boat): ").lower()
while method != "swim" and method != "boat":
    print("Invalid method. Please choose either 'swim' or 'boat'.")
    method = input("Choose a method (swim or boat): ").lower()
if method == "swim":
    print("Wrong choice! Game Over!")
    exit()

door_color = input("Which door you would like to opne (red, blue, or yellow? ").lower()
while door_color != "red" and door_color != "blue" and door_color != "yellow":
    print("Invalid door color. Please choose either 'red', 'blue', or 'yellow'.")
    door_color = input("Which door you would like to opne (red, blue, or yellow? ").lower()

if door_color == "red":
    print("Congratulations! You've found the treasure!")
else:
    print("Wrong door color! Game Over!")