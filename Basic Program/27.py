# Q.27 Write a program to convert Fahrenheit to Celsius.

while True:
    try:
        f = float(input("\nEnter Temperature in Fahrenheit: "))

        celsius = (f-32) * 5/9
        print("Temperature in Celsius: {:.3f}" .format(celsius)) #format() function
        print(f"Temperature in Celsius: {celsius:.3f}")          #f-string() function

    except ValueError:
        print("\nInvalid input...!! Please enter numeric value only")
        continue

    ch = input("\nDo you want to continue(Y/N) ").strip() .lower()

    if ch != 'y':
        print("\nProgram Closed")
        break