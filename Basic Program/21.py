# Q-21. W.A.P to accept a student’s name and roll number from the user and print the following formatted output using the format() function:

#  	Hello, Mr.Rohan
#  	Your Roll-No:142

name = input("Enter Your Name: ")
roll = int(input("Enter Your Roll-No: "))

# Using f-String() Function
print(f"Hello, {name}")
print(f"Your Roll-No: {roll}")


# Using Format() Function
print("Hello, Mr.{}".format(name))
print("Your Roll-No:{}".format(roll))