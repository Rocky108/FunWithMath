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

print(a,b,c)


d= 85
e=72
f=44
ans=0

if d>e:
    ans=12
else:
    if d==e:
        ans= 50
    else:
        if f<d*e:
            ans=100
        else:
            ans=75
print(ans)

import turtle
def showMonteyPi(numDarts):

    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2,-2,2,2)

    t.pu()
    t.goto(1,0)
    t.pd()
    t.goto(-1,0)

    t.pu()
    t.goto(0,1)
    t.pd()
    t.goto(0,-1)

    inCircle=0
    t.pu()

    for i in range(numDarts):
        x = random.random()
        y=random.random()

        distance= math.sqrt(x**2+y**2)
        t.goto(x,y)


        if distance<=1:
            inCircle=inCircle+1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi= inCircle / numDarts*4
    scn.exitonclick()
    return pi
showMonteyPi(10000)

#Your Task:
# modify Modify the simulation to plot points in the entire circle. you will have to adjust
# the claculated value of pi accordingly