
"""
Count Squirrels By Fur Colour

Gray
Cinnamon
Black

"""

import pandas

data = pandas.read_csv("./squirrel_data.csv")

print(data["Primary Fur Color"])

values = data["Primary Fur Color"].value_counts()
print(values)

values.to_csv("squirrel_count.csv")