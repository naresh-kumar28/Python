# Q.24 Write a program to calculate the area of a triangle using its base and height.

while True:
    
    try:
        base = float(input("\nEnter the base of Triangle: "))
        height = float(input("\nEnter the height of Triangle: "))

        if (base<=0) or (height<=0):
            print("\nInvalid input..!! Height and base must be positive numbers")
            continue

        input("\nPress any key to see the area of triangle...")
        area = (1/2)*base*height
        print("\nArea of Triangle :",area)

    except ValueError:
        print("\nInvalid input...!! Please enter only numeric value")
        continue

    ch = input("\nDo you want continue(y/n) ").strip() .lower()

    if ch != 'y':
        print("\nProgram closed")
        break