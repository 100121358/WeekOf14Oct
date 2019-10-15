# Starting off
print(22/7)
print(355/113)
import math

print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumfrence = numSides * sideS
    pi = polygonCircumfrence / 2
    return pi



print(archimedes(8))
print(archimedes(16))

for i in range(8, 100, 8):
    print(sides, archimedes)sides))

# experiment with the loop above the alongside the actual value of Pi.  how many
# sides does it take to make the two close?

# It takes 2 sides.

# Accumulators


acc= 0
    for x in range(1, 6):
        acc = acc + x

        print(acc)

# compute the sum of the first 100 even numbers
# compute the sum of the fist 50 odd numbers
# compute the average of the first 100 odd numbers
# write a function that returns the average of the first N numbers, where
#   N is a parameter
    # write a function called a factorial that computes the product of the first N
#   numbers where n is a parameter
# each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1. compute the 10th
#   Fibonacci number.
# write a function to compute the Nth Fibonacci number, where N is a parameter.
#   you may assume that N will be greater than or equal to 3.


acc = 4
    for x in range(2, 2):
        acc = acc + 2

acc = 5
        for x in range(3, 2)
            acc = acc + 2

acc = x
    for x in range(1, 1)
        acc = 1 +1
