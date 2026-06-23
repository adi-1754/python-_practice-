#  Level 1 ("conditional statements")

# Question 1: 
# while True:
#     num = int(input("Enter a number: "))
#     if num == 999:
#         print("Exiting the program.")
#         break
#     elif num < 0:
#         print("The number is negative.")
#     elif num == 0:
#         print("The number is zero.")
#     elif num > 0:
#         print("The number is positive.")

# def check_number(num):
#     if num < 0:
#         return "The number is negative."
#     elif num > 0:
#         return "The number is positive."
#     else:
#         return "The number is zero."
    
# print(check_number(-5))  # Output: The number is negative.
# print(check_number(0))   # Output: The number is zero.
# print(check_number(10))  # Output: The number is positive.



# Question 2 
# while True: 
#     num = int(input("Enter a number: "))
#     if num == 999:
#         print("Exiting the program.")
#         break
#     elif num % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")

# # Question 3 
# while True:
#     num = int(input("Enter a number: "))
#     if num == 999:
#         print("Exiting the program.")
#         break
#     elif num % 3 == 0 and num % 5 == 0:
#         print("The number is divisible by both 3 and 5.")
#     elif num % 3 == 0:
#         print("The number is divisible by 3.")
#     elif num % 5 == 0:
#         print("The number is divisible by 5.")
#     else:
#         print("The number is not divisible by either 3 or 5.")


# # Question 4
# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter a third number: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"The largest number is: {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The largest number is: {num2}")
# else:
#     print(f"The largest number is: {num3}")



