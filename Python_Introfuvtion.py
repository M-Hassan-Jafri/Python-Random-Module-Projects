import random as rnd

print("\n Her fileout")

l = [1,2,3,4,5,6,7,8,9]

numberRange = rnd.randint(1,5)
print(numberRange)

longRange = rnd.choice(l)
print(longRange)

while numberRange == longRange:
    print("You Win..!!!!")
    break