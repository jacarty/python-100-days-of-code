"""
Working with CSV files and analysing data with Pandas
"""

# open CSV and add to list
# results in a a messy list though

with open("./weather_data.csv") as file:
    data = file.readlines()
    print(data)
    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

######
# use the python csv module
######

import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    print(data)
    # create object
    # <_csv.reader object at 0x10510d2a0> 
    for row in data:
        print(row)
        """
        ['day', 'temp', 'condition']
        ['Monday', '12', 'Sunny']
        ['Tuesday', '14', 'Rain']
        ['Wednesday', '15', 'Rain']
        ['Thursday', '14', 'Cloudy']
        ['Friday', '21', 'Sunny']
        ['Saturday', '22', 'Sunny']
        ['Sunday', '24', 'Sunny']
        """

# add just the temperatures to the list temp
# no heading
# add as integer
import csv

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
print(data)
"""
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
"""

data = pandas.read_csv("./weather_data.csv")
print(data["temp"])

"""
0    12
1    14
2    15
3    14
4    21
5    22
6    24
"""

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data))
# <class 'pandas.core.frame.DataFrame'>

######
# Check data type
######
data = pandas.read_csv("./weather_data.csv")
print(type(data["temp"]))
# <class 'pandas.core.series.Series'>

"""
The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering. For R users, DataFrame provides everything that R’s data.frame provides and much more. pandas is built on top of NumPy and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.
"""

######
# Open Data
######
data = pandas.read_csv("./weather_data.csv")

######
# Pandas DataFrame (workbook) To_Dictionary
######
data_dict = data.to_dict()
print(data_dict)

######
# # Pandas Series (column) To_List
######
temp_list = data["temp"].to_list()
print(temp_list)


######
# calculate the average temperature
# manual way
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

total = 0 

# Pandas Series (column) To_List
for temperature in data["temp"].to_list():
    total += temperature

average = total / len(data["temp"].to_list())
print(average)

######
# calculate the average temperature
# with statistics
######

import pandas
import statistics

# Open Data
data = pandas.read_csv("./weather_data.csv")

temperatures = data["temp"].to_list()
statistics.mean(temperatures)

######
# calculate the average temperature
# with pandas
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].mean())

######
# find the maximum temperature
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

print(data["temp"].max())

"""
Get temp column
data["temp"]

Another way to call a column is simply
data.temp
"""

print(data.temp)

######
# return a row of data, e.g. Monday
######

print(data[data.day == "Monday"])

######
# return the row with highest temp of week
######

max_temp = data.temp.max()
print(data[data.temp == max_temp])

######
# alternative
######

print(data[data.temp == data.temp.max()])

######
# tapping in to a row
######

monday = data[data.day == "Monday"]
print(monday.condition)

monday = data[data.day == "Monday"]
print(monday.temp)


######
# get temp and convert to Fahrenheit
######

import pandas

# Open Data
data = pandas.read_csv("./weather_data.csv")

monday = data[data.day == "Monday"]
fahrenheit = (monday.temp[0] * (9/5)) + 32
print(fahrenheit)

"""
Create a Dataframe
"""

import pandas

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

#####
# output to CSV
#####

data.to_csv("new_data.csv")


"""
https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data

Count Squirrels By Fur Colour

Gray
Cinnamon
Black
"""

import pandas
data = pandas.read_csv("./squirrel_data.csv")
# print(data["Primary Fur Color"])

values = data["Primary Fur Color"].value_counts()
print(values)
values.to_csv("squirrel_count.csv")


########
# Instructor making dataframe and exporting
# Central Park Squirrel Data Analysis
########
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")