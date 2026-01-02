# Q.26 Write a program to convert kilometers to miles.

while True:

    try:
        km = float(input("\nEnter Value in KM: "))
        if km <= 0:
            print("\nInvalid input...!! Please enter Positive value only")
            continue

        miles = km*(0.621371)
        print(f"\n{km} KM = {miles:.3f} Miles")

    except ValueError:
        print("\nInvalid input..!! Please enter numeric value only")
        continue

    ch = input("\nDo you want to continue(Y/N) ").strip() .lower()

    if ch != 'y':
        print("\nProgram closed")
        break