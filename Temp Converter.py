def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

while True:
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        f_temp = float(input("Enter temperature in Fahrenheit: "))
        c_temp = fahrenheit_to_celsius(f_temp)
        print("Temperature in Celsius:", c_temp)
    elif choice == 2:
        c_temp = float(input("Enter temperature in Celsius: "))
        f_temp = celsius_to_fahrenheit(c_temp)
        print("Temperature in Fahrenheit:", f_temp)
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
