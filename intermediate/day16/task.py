# to do
# print report
# check sufficient resources
# process coins
# check transaction successful
# make coffee

"""
It wasn't explicit that all functionality needed to be replicated so I made a basic version.
Things I could add to replicate prior -  IF's for Off/Report, drink input validation, while loop etc.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# get their drink choice
drink_choice = input(f"What drink would you like to drink from {menu.get_items()}?: ")

# generate inventory report
coffee_maker.report()
money_machine.report()

# lookup drink choice
order = menu.find_drink(drink_choice)

# accessing the cost attribute of the order
cost = order.cost

# unused - accessing the ingredients attribute of the order
# ingredients = order.ingredients

# check sufficient resources for selected drink
coffee_maker.is_resource_sufficient(order)

# process coins and compare to drink cost
money_machine.make_payment(cost)

# make coffee based on order
coffee_maker.make_coffee(order)