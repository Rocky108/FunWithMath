# Starting off
print(22/7)
print(355/113)
import math

print(9801 / (2206*math.sqrt(2)))

def archimedes(numSides):
    innerAngleB=360.0/numSides
    halfAngleA=innerAngleB/2
    oneHalfSideS=math.sin(math.radians(halfAngleA))
    sideS=oneHalfSideS*2
    polygonCircumference=numSides*sideS
    pi=polygonCircumference/2
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))



#experiment with loop above along with the actual value of pi. how many
#sides does it take to make the two close?
print(archimedes(30))
# acumulators

acc = 0
for x in range(1, 6):
    acc = acc+x

print(acc)

#compute the sum of the first 100 even numbers
for numbers in range(1, 101):
    if numbers %2 == 0:
        print(numbers)
#compute the sum of the first 50 odd numbers
for numbers in range(0,51):
    if numbers %2 ==1:
        print(numbers)
#compute the average of the first 100 odd numbers

#write a function that returns the average of the first n numbers, where n is a parameter

#write a function called factoral that computes the product of the first n numbers, where n is a parameter
# each number in the fibonacci sequence is the sum of the previous two numbers
# the first two numbers in the sequence ar 1 and 1. compute the 10th
# fibonacci number.
#20
#write a function to compute the nth fibonacci number, where n is a parameter

# you may assume n will be greater than or equal to 3.

# montey carlo simulation

import random

print(random.random())

# boolean expressions
#> greater than
#>= greater than or equal to
#< less than
#<= less than or equal to
#== the same as
# != not equal to

dogweight = 25
print(dogweight != 25)
catweight=15

#compound boelean operators
#and
#or
#not

print(not catweight < 20)

# decision msking -- selection statements

a= 5
b=10
c=75

if a<=b:
    c=45
    if b> c:
        a=25
    else: a=-25
else:
    c= 1050
    if b==a:
        c=25

print(c)
