# Q-17. W.A.P to take two numbers from the user and perform all arithmetic operations with proper structure (int/float).


#Arithmetic Operation With Structure (int)

while True:
    while True:
        try:
            num1 = int(input("\nEnter 1st No: "))
            num2 = int(input("Enter 2nd No: "))

            if num1 >= 0 and num2 >=0:
                break
            else:
                print("Invalid input...!! Please enter Positive Number")

        except ValueError:
            print("Invalid input...!! Please enter numeric value only")

    input("Press any key to see arithmetic operation...")

    print(f"\nAddition: {num1} + {num2} = {num1+num2}")
    print(f"Substraction: {num1} - {num2} = {num1-num2}")
    print(f"Multiplication : {num1} * {num2} = {num1*num2}")
    print(f"Division : {num1} / {num2} = {num1/num2}")
    print(f"Modulus : {num1} % {num2} = {num1%num2}")

    ch = input("\nDo You Want to Continue(Y/N)? ").strip() .lower()

    if ch != "y":
        print("program close")
        break





#Arithmetic Operation With Structure (float)

# while True:
#     while True:
#         try :
#             num1 = float(input("\nEnter 1st No: "))
#             num2 = float(input("Enter 2nd No: "))

#             if (num1 and num2) >= 0:
#                 break
#             else:
#                 print("\nInvalid input...!! Please enter only positive value")

#         except ValueError:
#             print("\nInvalid input...!! Please enter numeric value")

#     input("\nPress Any key to see airthmetic operation..")

#     #Arithmetic Operation
#     print(f"\nAddition : {num1} + {num2} = {num1+num2:.2f}")
#     print(f"Substraction : {num1} - {num2} = {num1-num2:.2f}")
#     print(f"Multiplication : {num1} * {num2} = {num1*num2:.2f}")
#     print(f"Division : {num1} / {num2} = {num1/num2:.2f}")
#     print(f"Modulus : {num1} % {num2} = {num1%num2:.2f}")

#     ch = input("Do You Want To Continue(Y/N)? ").strip() .lower()

#     if ch != "y":
#         print("Program Closed...!")
#         break