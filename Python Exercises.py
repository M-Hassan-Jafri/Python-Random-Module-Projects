"""1. Write a Python program to print the following string in a
specific format (see the output).

Sample String : "Twinkle, twinkle, little star, How I wonder what you are!
Up above the world so high, Like a diamond in the sky. Twinkle, twinkle,
little star, How I wonder what you are"""

print("""\nTwinkle, twinkle, little star,
                 How I wonder what you are!
                         Up above the world so high, 
                         Like a diamond in the sky. 
Twinkle, twinkle, little star , 
                 How I wonder what you are""")


## 2. Write a Python program to find out what version of Python you are
## using.

import sys

print("\n\nPython Version: ", sys.version)
print("Python Version-info: ", sys.version_info)


## 3. Write a Python program to display the current date and time.

from datetime import datetime

print("\n\nCurrent Date & Time is: ", datetime.now())


## 4. Write a Python program that calculates the area of a circle based on
## the radius entered by the user. (Area = pi(r)^2)

"""import math

r = float(input("\n\nEnter radius (r) to calculate the area of the circle: "))
print("Area of the circle is: ", math.pi * r ** 2)
"""


## 5. Write a Python program that accepts the user's first and last name
## and prints them in reverse order with a space between them.

"""fname = input("\n\nInput your First Name: ")
lname = input("Input your Last Name: ")
print(f"\nHello {lname} {fname}")

name = input("\n\nEnter your first & last names: ")
rn = name[::-1]
print(rn)"""


## 6. Write a Python program that accepts a sequence of comma-separated
## numbers from the user and generates a list and a tuple of those
## numbers.  (Sample data : 3, 5, 7, 23)

"""numbers = (input("\n\nEnter 4 numbers (comma separated): "))

nos = numbers.split(', ')

l = list(nos)
t = tuple(nos)

print("\nYour numbers list: ", l)
print("Your numbers tuple: ", t)"""


## 7. Write a Python program that accepts a filename from the user and
## prints the extension of the file.
## (Sample filename : abc.java - Output : java)

"""import os

fn = input("\n\nEnter file name: ",)

e = fn.split('.')
print(e[1])

##ex = os.path.splitext(fn)     "Same problem solved by os module"
##print(ex[1])
"""


## 8. Write a Python program to display the first and last colors from the
## following list.
## color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red", "Green", "White", "Black"]
print("\n\n", color_list[0] + " " + color_list[3])


## 9. Write a Python program to display the examination schedule.
## (extract the date from exam_st_date).
## exam_st_date = (11, 12, 2014)
## Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = "11 / 12 / 2014"

print("\n\nThe examination will start from :", exam_st_date)


## 10. Write a Python program that accepts an integer (n) and computes
## the value of n+nn+nnn.
## Sample value of n is 5
## Expected Result : 615

"""n = input("\n\nEnter a number: ")
nn = str(n + n)
nnn = str(n + n + n)

print(f"\n n = {n} \n nn = {nn} \n nnn = {nnn}")

print(" n + nn + nn = ", int(n) + int(nn) + int(nnn))
"""

## 11. Write a Python program to print the documents (syntax, description etc.) of Python
## built-in function(s).
## Sample function : abs()
## Expected Result :
## abs(number) -> number
## Return the absolute value of the argument.

"""response = int(input("\n\nFunctions Descriptions: (select your choice 1-3) \n1. abs() \n2. type() "
                 "\n3. upper()\n\n"))

choice = True

while choice == True or 'y' or 'Y':
    if response == 1:
        print("SYNTAX & DESCRIPTION:\n abs(+/-number) -> +number \n Return the absolute value of the argument.\n")
    elif response == 2:
        print("SYNTAX & DESCRIPTION:\n type(variable) -> <class : type> \n Return the datatype of variable.\n")
    elif response == 3:
        print("SYNTAX & DESCRIPTION:\n upper(example) -> EXAMPLE \n Returns the string in uppercase.\n")
    else:
        print("Invalid input!! Choose from the correct options.")

    choice = input("Do you want to know about other functions.? (y/n)")
    response = int(input("\n\nFunctions Descriptions: (select your choice 1-3) \n1. abs() \n2. type() "
                         "\n3. upper()\n\n"))
"""

## 12. Write a Python program that prints the calendar for a given month and year.
## Note : Use 'calendar' module.

"""import calendar

print("\n\nWelcome to Calendar program.! {Select your Year & Month (in numbers)}\n")
y = int(input("Input Year: "))
m = int(input("Input Month: "))

choice = True

while choice == True or 'Y' or 'y':

    if y >= 1 and (m >= 1 and m <= 12):
        print("\nYour desired month/year calendar: \n\n", calendar.month(y, m))
    elif y <= 0:
        print("Invalid year.!!")
    elif y > 12:
        print("Invalid month.!!")

    choice = input("Did you want to view another calendar?? (y/n): ")

    print("\n\nWelcome to Calendar program.! {Select your Year & Month (in numbers)}\n")
    y = int(input("Input Year: "))
    m = int(input("Input Month: "))"""


## 14. Write a Python program to calculate the number of days between two dates.
## Sample dates : (2014, 7, 2), (2014, 7, 11)
## Expected output : 9 days

from datetime import date

d1 = date(2001, 7, 14)         ## date() function to specify/write customized date
d2 = date(2004, 6, 16)

days = (d2 - d1).days       ## logic of difference
print(f"\nThe difference between given dates is: {days} days")


## 15. Write a Python program to get the volume of a sphere with radius six.
## Volume (V) = 4/3 π r³

import math

r = 6
print("\n\nVolume of the sphere is: ", 4/3 * math.pi * r**3)


## 16. Write a Python program to calculate the difference between a given number and 17.
## If the number is greater than 17, return twice the absolute difference.

"""no2 = 17
no1 = int(input("\n\nEnter a number to find difference: "))

difference = no1 - no2

if no1 > 17:
    print(f"{no1} - {no2} =", abs(difference), "its", abs(difference))
else:
    print(f"{no1} - {no2} =", difference)"""


## 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)

print("\n\n", near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))


## 18. Write a Python program to calculate the sum of three given numbers. If the values are
## equal, return three times their sum.

"""def sum(a=1,b=1,c=1):

    if a == b == c:
        print("\nThe 3 times of the sum (multiplication): ", (a+b+c)*3)
    else:
        print("\nThe sum: ", a+b+c)

print("\n\t\t\t!-----WELCOME TO 3 NUMBERS SUMMATION PROGRAM-----!\n")

i = int(input("Enter 1st number: "))
j = int(input("Enter 2nd number: "))
k = int(input("Enter 3rd number: "))

sum(i, j, k)"""


## 19. Write a Python program to get a newly-generated string from a given string where
## "Is" has been added to the front. Return the string unchanged if the given string
## already begins with "Is".


""" i = input("\n\nPLease enter a string/word: ")
print("\nYour string: ", i)

if len(i) >= 2 and i[:2] == "Is":
    print("Your unchanged string:", i)
print("The changed string: " + "Is" + i)"""


## 20. Write a Python program that returns a string that is n (non-negative integer)
# copies of a given string.

def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result

print()
print()

print(larger_string('Hassan', 4))
print(larger_string('.java', 10))


## 21. Write a Python program that determines whether a given number (accepted from the
## user) is even or odd, and prints an appropriate message to the user.

"""i = int(input("\n\nEnter a number - (to know whether its Even or Odd): "))

if i % 2 == 0:
    print("Even number..")
else:
    print("Odd number..")"""


## 22. Write a Python program to count the number 4 in a given list.

l = [1, 2, 3, 4, 5, 4, 7, 4, 4, 1, 2, 3, 4]
print("\n\nThe number ' 4 ' appeared in the list", "'", l.count(4), "'", "times!!")


## 23. Write a Python program to get n (non-negative integer) copies of the first 2
## characters of a given string. Return n copies of the whole string if the length is less
## than 2.

def copies(s, n):
    new_str = ""

    for i in s:
        new_str = new_str + i

    if len(new_str) < 2:
       whole_str = new_str * n
       print(f"\n\nThe {n} copies of the whole string:", whole_str)
    else:
        f2c = new_str[:2]
        print(f"\nThe {n} copies of the first 2 characters of the given string:", f2c * n)

copies("K", 4)
copies("Hassan", 6)


## 24. Write a Python program to test whether a passed letter is a vowel or not.

letter = input("\n\nEnter an English alphabet: ")

if letter.lower() == ('a' or 'e' or 'i' or 'o' or 'u'):
    print(f"{letter} is a: 'vowel'")
elif letter.lower() == 'y':
    print(f"{letter} is a: 'semivowel'")
else:
    print(f"{letter} is a: 'consonant'")

