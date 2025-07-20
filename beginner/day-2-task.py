print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in £?\n")) #str
percentage_tip = float(input("How much tip would you like to give? 10, 12 or 15?\n")) 
people = int(input("How many people want to split the bill?\n"))

total_bill = bill * (1 + (percentage_tip / 100))
bill_split = total_bill / people
fianl_amount = round(bill_split, 2)

print(f"Each person should pay £{fianl_amount}")