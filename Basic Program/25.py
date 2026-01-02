# Q.25 Write a program to find area of circle

while True:
    while True:
        try:
            r = float(input("\nEnter a Radius: "))

            if r <= 0 :
                print("\nInvalid input..!! Please enter positive numbers only")
                continue

            else:
                break

        except ValueError:
            print("\nInvalid input...!! Please enter only numeric value")

    input("\nPress any key to see the area of circle...")

    area = (3.14)*r*r

    print("\nArea of Circle :",area)

    ch = input("\nDo you want continue(y/n) ").strip() .lower()

    if ch != 'y':
        print("\nProgram closed")
        break