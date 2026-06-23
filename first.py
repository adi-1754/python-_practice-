#  Smart Temperature Converter 
# Take input in Celsius and print its equivalent in Fahrenheit and Kelvin. 
# (Use explicit type conversion and arithmetic operators.) 
# Formula: 
# ● Fahrenheit = (C × 9/5) + 32 
# ● Kelvin = C + 273.15 
#ans 

# cel = int(input("Enter a temperture in celcius - "))
# far_temp = float(( cel * 9/5 ) + 32 )
# kel_temp = float(cel + 273.15)
# print(far_temp)
# print(kel_temp)


# Write a program that takes total bill amount and number of friends as input. 
# Calculate how much each person will pay. 
# Also print the data type of each variable used. 
#ans 

# total_bill = float(input("enter a total amount of bill "))
# total_friends = int(input("Enter a number of your friends "))
# final_bill = total_bill / total_friends
# print("Each will pay ",final_bill)


# Write a Python program that takes a user’s name as input and prints: 
# 1. The first character 
# 2. The last character 
# 3. The total length of the name
#ans 

# first_name = input("Enter your first name ")
# last_name = input("Enter your last name ")
# full_name = first_name + last_name
# print("Full Name - ",full_name)
# print("length of your name is - ",len(full_name))


# Write a program that takes your favorite food name as input and prints: 
# ● The middle 3 characters 
#  ● The last 2 characters 
#ans 

# name = input("Enter a your favorite food name - ")
# print(name[2:5])
# print(name[-3:-1])


# Write a program that: 
# ● Takes a sentence as input 
# ● Converts it to lowercase 
# ● Replaces all spaces " " with underscores "_" 
# ● Prints the new string 
#ans 

# sen = input("Enter a sentence ")
# sen_lower = sen.lower()
# sen_rep = sen_lower.replace(" ","_")
# print(sen_rep)


# Write a program that takes a sentence and prints: 
# ● Total characters (len()) 
# ● Uppercase version 
# ● Lowercase version
#ans 

# sen = input("Enter a sentence - ")
# print("Total length of string ",len(sen))
# print("UPPERCASE ",sen.upper())
# print("lowercase",sen.lower())


# Write a Python program that takes any word or sentence as input and prints: 
# ● The first character 
# ● The last character 
# ● The total number of characters 
#ans 

# sen = input("Enter a string - ")
# print("First character",sen[0])
# print("Last character",sen[-2:-1])
# print("Length of string",len(sen))


# Write a Python program that takes a number as input and prints: 
# ● “Positive” if number > 0 
# ● “Zero” if number == 0 
# ● “Negative” if number < 0 
#ans 

# num  = int(input("Enter a number : "))
# if num > 0 :
#     print("Positive")
# elif num == 0 :
#     print("Zero")   
# else : 
#     print("Negative")    


# 1. Ask the user for their 3 favorite movies and store them in a list. 
# 2. Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and 
# lowest marks using max() and min(). 
# 3. Write a program to check grade based on marks (A/B/C/D) using if-elif-else. 
#ans

#1. 
# movie = []
# movie.append(input("Enter your favorite movies - "))
# print(movie)
#2.
# marks = (87, 64, 33, 95, 76)
# print("Highest marks - ",max(marks))
# print("Lowest marks - ",min(marks))
#3.
# marks = int(input("Enter your marks -"))

# if marks >= 90 and marks <= 100:
#     print("Grade A")
# elif marks >= 60 and marks < 90:
#     print("Grade B")
# elif marks >= 40 and marks < 60:
#     print("Grade C")  
# else:
#     print("Grade D")       
# 


# Create a dictionary named marks to store marks of 3 subjects. 
# Add the subjects one by one and print the final dictionary. 
#ans 

# dict = {}
# dict["Maths"] = int(input("Enter marks of Maths - "))
# dict["Science"] = int(input("Enter marks of Science - "))   
# dict["English"] = int(input("Enter marks of English - "))
# print(dict)


#
#Create a dictionary storing meanings of 3 English words.
#ans

# dict = {}
# for i in range(3):
#     word = input("Enter a word - ")
#     dict[word] = input("Enter the meaning of the word - ")

# print(dict)


#Create a set of numbers and show union and intersection with another set.
#ans 

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# print("Union of set1 and set2 - ",set1.union(set2))
# print("Intersection of set1 and set2 - ",set1.intersection(set2))

# Write a program to print this pattern using a while loop: 
# * 
# * * 
# * * * 
# * * * * 
# (Hint: use one while loop and string multiplication like '*' * count)
#ans

# count = 1 
# while count <= 4:
#     print("* " * count)
#     count += 1

#Mini Project – Countdown Timer (with 1-second gap) 
# Goal: 
# Print a countdown before something “exciting” happens (like “Launching…” or 
# “Happy New Year!”). 
# Concepts Used: for loop, range(), and the time module. 

# import time
# for i in range(3, 0, -1):
#     print(i)
#     time.sleep(2)
# print("Happy New Year!")




# Expense Tracker (Mini Project)

# expenses = []

# print("Welcome to the finace Tracker : ")

# while True:
#     print("--- Menu ---")
#     print("1. Add Expenses ")
#     print("2. View All Expenses")
#     print("3. View Total Expenses")
#     print("4. Exit ")
#     print("--------------------------")


#     choice = int(input("Enter your Choice (1-4) "))
#     if(choice == 1):
#         date = input("Enter a date of expense ")
#         category = input("Tell me which type of expense (food , travel, books)")
#         description = input("Explain in description ")
#         amount = float(input("Enter your expense "))
#         expense = {
#             "date":date, 
#             "category":category,
#             "description":description,
#             "amount":amount
#         }
#         expenses.append(expense)
#         print("Expenses added sucessfully ")
#     elif(choice == 2):
#         print(expenses)

#     elif(choice == 3):
#         total = 0 
#         for i in expenses: 
#             total = total + i["amount"] 
#         print(total)  
#     elif(choice == 4):
#         print("Thank you for using the Expense Tracker. Goodbye!")
#         break    

# write a function learn() that print the python topics

# def learn():
#     print("variable , conditional statement , loop , list, tuple , dictionary , set ")
# learn()    


# Write a function show_age(name, age) that prints: "Saumya Singh is 21 
# years old.


# def show_age(name, age):
#     print(f"{name} is  {age} years old ")

# show_age("aditya", 18)   

# Write a function square(num) that returns the square of a number.

# def func_seq(num):
#     return num ** 2 

# result = func_seq(7) 
# print(result)



#Write a function that takes a string and returns the count of vowels and 
# consonants separately. 

# def count_vowels(string_us):
#     vowels = ["a",'e','i','o','u','A','E','I','O','U']
#     count = 0 
#     count_cons = 0 
#     for eachChar in string_us:
#         if (eachChar in vowels):
#             count += 1
#         else:
#             count_cons += 1    

#     print(f"vowels {count} constants {count_cons} ")  

# count_vowels("aditya") 


# Define a function convert_to_upper(word) that returns the uppercase 
# version of the string.


# def fun(word):
#     return word.upper()

# demo = fun("aditya")
# print(demo)

# Recursion 

# def fib(n):
#     if (n == 1 or n == 2 ):
#         return 1
#     else:
#         return fib((n-1)) + fib((n - 2) )
# 
# print(fib(6))



