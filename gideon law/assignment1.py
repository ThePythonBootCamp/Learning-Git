# def Area (r):
#     return math.pi * r * r

import math

def area_of_(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the value of radius: "))
area = math.pi * radius ** 2
print(area)
print(f"The area of a circle with radius {radius} is: {area} ")
    
