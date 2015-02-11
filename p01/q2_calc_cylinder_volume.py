radius = float(input("Enter the radius (in cm): "))
length = float(input("Enter the length (in cm): "))
from math import pi
area = float(radius * radius * pi)
volume = area * length
print("The volume of the cylinder is", "{0:.2f}".format(volume), "cm^3")
