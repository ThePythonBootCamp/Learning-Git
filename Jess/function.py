#Calculate the Area of a Circle
def area_of_circle(radius):
    #Calculate the area of a circle given its radius.
    pi = 3.14159  
    # Using an approximate value of π
    return pi * radius**2

radius = 5
print(f"The area of the circle with radius {radius} is {area_of_circle(radius):.2f}")

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    #Convert Celsius to Fahrenheit.
    return (celsius * 9/5) + 32

celsius = 25
print(f"{celsius} degrees Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} degrees Fahrenheit")