# Print the title of the program
print("Temperature Converter")

# Print the menu options
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Take user's choice as an integer
choice = int(input("Enter your choice :- "))

# If user chooses option 1: Celsius to Fahrenheit
if choice == 1:
    # Take temperature input in Celsius
    celsius = float(input("Enter the temperature in Celsius: "))
    # Convert Celsius to Fahrenheit using formula
    fahrenheit = (celsius * 9/5) + 32
    # Display the result
    print(f"{celsius} C = {fahrenheit} F")

# If user chooses option 2: Fahrenheit to Celsius
elif choice == 2:
    # Take temperature input in Fahrenheit
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    # Convert Fahrenheit to Celsius using formula
    celsius = (fahrenheit - 32) * 5/9
    # Display the result
    print(f"{fahrenheit} F = {celsius} C")

# If user enters an invalid choice
else:
    print("Invalid choice!")
