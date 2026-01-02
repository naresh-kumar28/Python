# Q.23 Write a program to find the HCF (Highest Common Factor) of two given numbers.


# while True:

#     while True:
#         try:
#             num1, num2 = map(int, input("\nEnter 1st & 2nd No: ").split())

#             if (num1<=0) or (num2<=0):
#                 print("\nInvalid input...!! Please enter Positive Number")
#                 continue

#             else:
#                 break

#         except ValueError:
#             print("\nInvalid input..!! Please enter numeric value only")
            
#     greatest_num = max(num1,num2)

#     while True:
#         if (num1%greatest_num==0 and num2%greatest_num==0):
#             hcf = greatest_num
#             break

#         greatest_num -=1

#     print(f"\nHCF = {greatest_num}")

#     ch = input("\nDo you want to continue(Y/N) ").strip() .lower()

#     if ch != "y":
#         print("Program Closed")
#         break





while True:

    while True:
        try:
            num1, num2 = map(int, input("\nEnter 1st & 2nd No: ").split())

            if (num1<=0) or (num2<=0):
                print("\nInvalid input...!! Please enter Positive Number")
                continue

            else:
                break

        except ValueError:
            print("\nInvalid input..!! Please enter numeric value only")
            

    for i in range(max(num1,num2), 0, -1 ):
        if(num1%i==0 and num2%i==0):
            hcf = i
            break
    

    print(f"\nHCF = {hcf}")

    ch = input("\nDo you want to continue(Y/N) ").strip() .lower()

    if ch != "y":
        print("Program Closed")
        break