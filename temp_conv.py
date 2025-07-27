print("Temperature Converter")
print("1.Celcius to Fahrenheit")
print("2.Fahrenheit to Celcius")

choice = int(input("Enter your choice:"))
if choice == 1:
  celcius =float(input("Enter the temperature in celcius:"))
  fahrenheit =(celcius*9/5)+32 
  print(f"{celcius} C = {fahrenheit} F ")

elif choice ==2:
  fahrenheit =float(input("Enter the temperature in fahrenheit: "))
  celcius =(fahrenheit-32)*5/9
  print(f"{fahrenheit} F = {celcius} C")

else:
  print("Invalid choice!")
  