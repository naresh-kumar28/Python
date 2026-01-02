# Q.22 Write a program to find the LCM (Least Common Multiple) of two given numbers.

# while True:
#     while True:
#         try:
#             num1, num2 = map(int, input("Enter 1st & 2nd No: ") .split())

#             if (num1 <= 0 ) or (num2 <= 0):
#                 print("\nInvalid input..! Please enter positive integers only.\n")
#                 continue

#             else:
#                 break

#         except ValueError:
#             print("\nInvalid input..!! Please enter positive integer")

#     #find the greater value
#     greater = max(num1,num2)

#     while True:
#         if(greater % num1 == 0 and greater % num2 == 0):
#             lcm = greater
#             break
#         greater+= 1

#     ch = input("\nDo you want to continue (y/n)? ").strip() .lower()

#     if (ch != "y"):
#         print("\nProgram Closed")
#         break





while True:
    while True:
        try:
            num1, num2 = map(int, input("\nEnter 1st & 2nd No: ").split() )

            if (num1 <= 0) or (num2 <= 0):
                print("\nInvalid input..!! Please enter positive number...")
                continue

            else:
                break

        except ValueError:
            print("Invalid input...!! Please enter numeric value only")

    for i in range(max(num1, num2), (num1*num2)+1 ):
        if (i%num1 == 0 and i%num2==0):
            lcm = i
            break
    
    print(f"LCM : {lcm}")

    ch = input ("\nDo You Want to continue(Y/N) ").strip() .lower()

    if(ch != "y"):
        print("Program Closed")
        break

        















# x = int(input("Enter 1st No: "))
# y = int(input("Enter 2nd No: "))

# input("\nPress any key to see the LCM...")

# # for i in range(max(x,y) , (x*y)+1):
# #     if(i%x==0 and i%y==0):
# #         lcm = i
# #         break

# # print(f"Lcm is {lcm}")

# max_num = max(x,y)

# if (max_num % x == 0 and max_num % y ==0):
#     lcm = max_num
#     break
# max_num+=1
# print(f"Lcm is {lcm}")