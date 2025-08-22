"""
Inheritance & Slicing

class Fish():
    def __init__(self):

    
class Fish(Animal):
    def __init__(self):
        super().__init__()

"""

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe() # this does everything the breathe method above does
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)

"""

slicing works on lists and tuples
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

piano_keys[2:5]
returns c, d, e
2, 3 and 4

piano_keys[2:5:2]
returns c, e
every other one

piano_keys[::-1]
returns, g, f, e, d, c, b, a

"""

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:])

# returns 're', 'mi', 'fa', 'so', 'la', 'ti'

piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[:5])

# returns 'do', 're', 'mi', 'fa', 'so'
