# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    #Convert Celsius to Fahrenheit.
    return (celsius * 9/5) + 32

celsius = 25
print(f"{celsius} degrees Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} degrees Fahrenheit")