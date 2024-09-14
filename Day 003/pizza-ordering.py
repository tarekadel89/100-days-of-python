# pizza ordering calculation
pizza_size = input("Enter the size of the pizza (S, M, L): ").upper()
while pizza_size not in ['S', 'M', 'L']:
    print("Invalid input. Please enter a valid pizza size (S, M, L).")
    pizza_size = input("Enter the size of the pizza (S, M, L): ")
    
extra_pepperoni = input("Do you want extra pepperoni? (Y/N): ").upper()
while extra_pepperoni not in ['Y', 'N']:
    print("Invalid input. Please enter Y or N")
    extra_pepperoni = input("Do you want extra pepperoni? (Y/N): ").upper()

extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()
while extra_cheese not in ['Y', 'N']:
    print("Invalid input. Please enter Y or N")
    extra_pepperoni = input("Do you want extra cheese? (Y/N): ").upper()
    
# calculate the cost

pizza_price = 0
if pizza_size == 'S':
    pizza_price = 10
    if extra_pepperoni == 'Y':
        pizza_price += 2
else:
    if pizza_size == 'M':
        pizza_price = 15
    else:
        pizza_price = 20
    if extra_pepperoni == 'Y':
        pizza_price += 3
        
if extra_cheese == 'Y':
    pizza_price += 1

print("The cost of your pizza is:", pizza_price)