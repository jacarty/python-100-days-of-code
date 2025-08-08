"""
Day 17 Content - Building Classes

The challenge will be a building a Quiz Game with OOP.
"""

"""
Simply defined by class Name:
Then code follows.

Classes should have each letter of the first word Capitilised
Reminder it's called: PascalCase 

vs camelCase which has the first word lower, and the rest first char upper

vs snake_case which is lower case and separated by _ (variables, py files etc.)

camelCase - commonly used for variable and function names in languages like JavaScript and Java

PascalCase - often used for class names and type names in languages like Python, C# and .NET

class Car:
"""
# Pass simply used to avoid the formatting error of expecting code after the :
class User: # define class
    pass

user1 = User() # create object from Class

"""
How to create an attribute for your class

An attribute is a variable associated with an object

Examples:

But notice, unless defined in the Class you can create any attributes, 
and it's also errorprone/potentially inconsitent

The notion of a Class is to specify these pieces of information 
when creating the object from the Class in the form of Constructors
"""

class User: # define class
    pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"

print(user1.username)

user2 = User()
user1.id = "002"
user1.name = "steve"

"""
Constructor
A part of the blueprint that specifies what should happen when the object is being constructed

When the object is being initialised from the Class
you set the variables, counters, switches to their starting values 

You create the Constructor by using the init function - it's a special method

class Car:
    def __init__(self):
    #intialise attributes

Self is the Object being created
"""

class User: # define class
    
    # this is where we create or intialise the starting values for our attributes
    # the __init__ function is called ever time you create a new object from this Class
    def __init__(self):
        print("new user being created")

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
Will result in:

new user being created
alan
new user being created
steve

Reminder:
Attributes - things a Class has
Methods - things a Class does

Example on setting attributes
E.g. a car has 5 seats
You pass in the parameter alongside the Object being created (initialised)
The parameter gets passed in when the Object is constructed from the Class
You can pass in as many parameters as you want
When you recieve that data you can use it to set that Objects attributes
"""

# sets the numher of seats to 5
class Car:
    def __init__(self, seats):
        self.seats = seats
        print(seats)

my_car = Car(5)

# which is effectively the same result as

my_car.seats = 5

"""
/\ /\ /\ The key Point on above
The __init__ method is convenient, automated way to set attributes when an object is created. 
But the actual mechanism of setting self.seats = seats inside __init__ 
is the same as setting my_car.seats = 5 outside of it.
"""

class User: 

    def __init__(self):
        pass

user1 = User() # create object from Class
user1.id = "001"
user1.username = "alan"
print(user1.username)

#returns alan

""" we're creating attributes at the time of constuction 
typical convention is for the name of parameter to match name of attribute (doesnt have to)
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user1 = User("001", "alan") 
print(user1.username)

"""Because we've now set the parameters in the constructor, 
you have to use them when creating the object from the Class

If not you will receive an error:
TypeError: __init__() missing 2 required positional arguments: 'user_id' and 'username'
See below
"""
user2 = User()
user2.id = "002"
user2.name = "steve"
print(user2.name)

"""
You can also set default values that done have to be passed as parameters
"""

class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 

user1 = User("001", "alan") 
print(user1.followers)

# returns 0

"""
methods = things the Class does

e.g attribute = has 5 seats
method = change to 2 seats

example
"""

class User: # define class

    def enter_race_mode(): # method
        self.seats = 2 # gets seats attribute and changes to 2

my_car.enter_race_mode()


"""
in practice - instagram followers
"""
class User: # define class

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 
        self.following = 0

    # you always use 'self' as first parameter in a method so the function knows the Ojnect that called it
    # assume we follow a user (instagram)
    def follow(self, user):
        user.followers += 1     # the user we're following goes up by 1
        self.following += 1     # the user count we're following goes up by 1

user1 = User("001", "alan") 
user2 = User("002", "dan") 

user1.follow(user2)

print(f" user 1 followers: {user1.followers}")
print(f" user 1 following: {user1.following}")

print(f" user 2 followers: {user2.followers}")
print(f" user 2 following: {user2.following}")

 """
 returns
 user 1 followers: 0
 user 1 following: 1
 user 2 followers: 1
 user 2 following: 0
 """
