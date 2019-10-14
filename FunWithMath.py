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
