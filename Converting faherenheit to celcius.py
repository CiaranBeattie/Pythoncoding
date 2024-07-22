def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # Formula for converting Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # Formula for converting Celsius to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# prompt the user to pick which calculation they would like to preform
choice = input("Enter '1' to convert Fahrenheit to Celsius or '2' to convert Celsius to Fahrenheit: ")


# preform output based on the users choice of calculation
if choice == '1':
    # If user chooses conversion of Fahrenheit to Celsius
    fahrenheit_input = float(input("Please input your temperature in Fahrenheit: "))
    print("Your converted temperature is: {:.2f} C".format(fahrenheit_to_celsius(fahrenheit_input)))
elif choice == '2':
    # if user chooses Celsius to Fahrenheit
    celsius_input = float(input("Please input your temperature in Celsius: "))
    print("Your converted temperature is: {:.2f} F".format(celsius_to_fahrenheit(celsius_input)))
else:
    # error handling if user inputs the wrong value
    print("Invalid choice. Please enter either '1' or '2'.")
