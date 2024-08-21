def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) *1.8
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
        celsius_temp = float(input("Enter temperature in Celsius: "))
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{celsius_temp} Celsius is equal to {fahrenheit_temp:.2f} Fahrenheit")
elif choice == 2:
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {celsius_temp:.2f} Celsius")
   
