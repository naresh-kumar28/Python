# Q.28 Write a program to convert Celsius to Fahrenheit

while True:
    try:
        celsius = float(input("\nEnter Temperature in Celsius: "))

        fahrenheit = (celsius*9/5)+32
        print(f"\n{celsius}°C = {fahrenheit}°F")

    except ValueError:
        print("\nInvalid input...!! Please enter only numeric value")

    ch = input("\nDo you want to continue(Y/N) ")

    if ch != 'y':
        print("\nProgram Closed")
        break