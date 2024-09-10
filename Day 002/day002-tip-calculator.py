## Tip calculator program
print("Welcome to the tip calculator!")

bill = input("Enter the total bill amount: $")
while not bill.replace('.', '', 1).isdigit():
    print("Invalid input. Please enter a valid bill amount.")
    bill = input("Enter the total bill amount: $")
    
tip_percentage = input("Enter the desired tip percentage (10, 12, 15): %")
while tip_percentage not in ['10', '12', '15']:
    print("Invalid input. Please enter a valid tip percentage (10, 12, 15).")
    tip_percentage = input("Enter the desired tip percentage (10, 12, 15): %")
    
num_people = input("Enter the number of people sharing the bill: ")
while not num_people.isdigit() or int(num_people) <= 0:
    print("Invalid input. Please enter a valid number of people (greater than 0).")
    num_people = input("Enter the number of people sharing the bill: ")

bill_with_tip =  float(bill) + (float(bill) * float(tip_percentage) / 100) 

person_share = bill_with_tip / int(num_people)

person_share = round(person_share, 2)  # round to two decimal places

print(f"The total bill with tip is ${bill_with_tip:.2f}.")
#print(f"Each person's share is ${person_share:.2f}.")
print(f"Each person's share is ${person_share}")  # format the output to