## Arithmetic Operations
"""
a = 4**4
b = 5//5
c = 6%6

print(a)
print(b)
print(c, "\n")


# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference (different values of set A)
print("Difference :", A - B)

# symmetric difference (Different values in both sets)
print("Symmetric difference :", A ^ B)
"""

h = {"Name" : "Hassan",
     "Gender" : "Male",
     "Age" : 21,
     "Caste" : "Syed"}

c = [1, 2, "ask-hf", 2.34, False]

##for elem in A:
  ##  print(elem)

for items in h.items():
    print(items)

print("\n")

for l in c:
    print(l)

print()


## FUNCTIONS

def test(a,b,c):
    print("Multiplying numbers: ")
    d = a*b*c
    print(d)

test(2,3,4)

print()

## CLASSES IN PYTHON

"""All classes have a function called '__init__()', which is always executed
   when the class is being initiated. Use the '__init__()' function to 
   assign values to object properties, or other operations that are 
   necessary to do when the object is being created. Its like a constructor."""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)