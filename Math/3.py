import math
a = int(input("Input number of sides: "))
b = float(input("Input the length of a side: "))
z = (a * b * b) / (4 * math.tan(math.pi / a))
print("The area of the polygon is:", int(z))