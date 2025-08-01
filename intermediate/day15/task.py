"""
Create a coffee maching

Coffee Machine Program Requirements

1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.

2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.

3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.

5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.

7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""
from data import MENU, resources

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.


def report(balance):
    """Reports back the coffee machine inventory."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${balance}")

def insert_coins():
    """Returns total"""
    print("Please insert some coins.")
    try:
        quarters = int(input("How many quarters?: "))
    except ValueError:
        quarters = 0 
    try:
        dimes = int(input("How many dimes?: "))
    except ValueError:
        dimes = 0
    try:
        nickles = int(input("How many nickles?: "))
    except ValueError:
        nickles = 0 
    try:
        pennies = int(input("How many pennies?: "))
    except ValueError:
        pennies = 0
    #sum of coins added to machine
    return float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
    # print(f"sum of coins = {sum_of_coins}")

def make_coffee():
    
    # starting amount of money in machine
    machine_total = 0

    while True:
        
        # get coffee selection
        coffee = input("What would you like? espresso, latte or cappuccino: ").lower()

        # maintenance mode
        if coffee == "off":
            print("Going into maintenance mode. Goodbye")
            break

        # print inventory
        elif coffee == "report":
            report(balance=machine_total)
            continue

        # if invalid coffee
        elif coffee not in MENU:
            continue

        # compare coffee
        else:
            selection = (MENU[coffee]["ingredients"])
            for item in selection:
                if selection.get(item) > resources[item]:
                    print(f"Sorry there is not enough {item}.")
                    break
                # else:
                #     print(f"{item} ok")

        # Get total of inserted coins
        sum_of_coins = insert_coins()

        price = (MENU[coffee]["cost"])
        # print(f"drink price = {price}")
        
        # check if enough coins added to buy coffee
        if sum_of_coins < price:
            print("Sorry that's not enough money. Money refunded.")
        # return change and update machine money
        elif sum_of_coins > price:
            calculate_change = round(sum_of_coins - price, 2)
            print(f"Change being dispensed: ${calculate_change}.")
            machine_total += price

        # resources update to reduce inventory
        for item in selection:
            resources[item] = resources[item] - selection.get(item)
            # print(f"{item} is now = {resources[item]}")
        print(f"Here is your {coffee}. Enjoy!")

make_coffee()