# List of Temperatures recorded over a given week creating the variable temperatures
Temperatures = [("Monday", 16), ("Tuesday", 12), ("Wednesday", 5), ("Thursday", 10), ("Friday", 12), ("Saturday", 14),
                ("Sunday", 15)]


# Creating a function to calculate the average temperature
def calculate_average(temperatures):
    # adding the total number of temperatures together
    total_temperature = sum(temperature for day, temperature in temperatures)
    # calculating the number of days to divide by
    num_days = len(temperatures)
    # creating formula to calculate the average temperature in the week
    average = total_temperature / num_days
    # returning the calculated average temperatures
    return average


# calling the function to calculate the average temperature
Average_temp = calculate_average(Temperatures)

# Displaying the final answer in a string concatenation
print(f"The average temperature is {Average_temp:.2f} in degrees celcius")
