FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

input_temp = input("Enter the temperature to convert: ")
input_factor = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

try:
    input_temp = float(input_temp)
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit(1)

if input_factor == 'C':
    print(f"{input_temp}C is {convert_to_fahrenheit(input_temp)}F")
elif input_factor == 'F':
    print(f"{input_temp}F is {convert_to_celsius(input_temp)}C")
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    exit(1)
    


