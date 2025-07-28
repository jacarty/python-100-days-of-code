# ### Functionality
# - Each person writes their name and bid.
# - The program asks if there are others who need to bid. 
#   If so, then the computer clears the output (prints several blank lines) then loops back to asking name and bid.
# - Each person's name and bid are saved to a dictionary.
# - Once all participants have placed their bid, the program works out who has the highest bid and prints it.

import os
import day_9_art

print(day_9_art.logo)
print("Welcome to the secret auction program.\n")

more_bidders = True
open_bids = {}

while more_bidders:

    name = input("What is your name?\n")
    bid = int(input("What is your bid £?\n"))

    # Add offer to open_bid dictionary
    open_bids[name] = bid
    # print(open_bids)

    # check for more bidders
    bidders = input("Are there more bidders? Type 'yes' or 'no'.\n").lower()

    # clear screen for 'blind auction' and accept next bid
    if bidders == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        more_bidders = True
        continue

    # exit loop to calculate winner
    elif bidders == "no":
        more_bidders = False

    else:
        print("Please check and try and again.")
        more_bidders = False

# without key= it would simply max the key based on alphabet
# using key=open_bids.get gets it to max the value
winner = max(open_bids, key=open_bids.get)
winning_price = open_bids[winner]
print(f"The winner is {winner} with a winning bid of £{winning_price}.")


"""
Instructor used this loop instead of max function to do the same
highest_bid = 0
winner = ""
for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
"""