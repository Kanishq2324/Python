# Comments
#hello myself kanishq

# """
# Hello i am kanishq
# kanishq is a good person
# """



# Variables
# """k = 8
# a = 8.0
# b = 8.14
# name = "Kanishq"
# v = 34j

# NameName = "Kanishq"    #pascal case
# nameName = "Kanishq"    #camel case
# name_name = "Kanishq"   #snake case

# print(type(k))
# print(type(name))
# print(type(a))
# print(type(b))
# print(type(v))"""




# Strings & Type Conversions

# k = 65
# a = "k"

# print(chr(k))
# print(ord(a))

# name = "Kanishq"

# print(name[0])

# temp = "kanishq good"
# print(temp[0:7:1])   # [start : stop : slice]



# a = 12

# a = str(a)

# print(type(a))




# # falsy values -> false, 0, 0.0, "", [], (), {} 




# name = "Kanishq"
# age = 23

# print("Hello my name is",name, "and my age is", age)
# print(f"my name is {name} and my age is {age}") # formatted string



# age = int(input("what is your age "))

# print(age)






# if - else 
# a = 23

# if (a != 22) :
#     print(a)
# else: print(21)


# name = 23
# if(name > 25):
#     print("incorrect")
# elif (name > 21 and name < 25):
#     print("Correct")
# else:
#     print("incorrect")



# temp = int(input("Enter the temperature "))

# if(temp < 0) :
#     print("Freezing Cold")
# elif(temp >= 0 and temp < 10):
#     print("Very Cold")
# elif(temp >= 10 and temp < 20):
#     print("Cold")
# elif(temp >= 20 and temp < 30):
#     print("Pleasant")
# elif(temp >= 30 and temp < 40):
#     print("Hot")
# else :
#     print("Very Hot")



# greet = str(input("what is your gender "))
# if(greet == "M"):
#     print("Hello Sir")
# else :
#     print("Hello Maam")




# Loops - for loop, while loop

# 1. For Loop
# a = range(1, 20, 1)

# for i in a:
#     print(i)


# for i in range(1, 21, 2):
#     print(i)


# for i in range(16, 0, -1):
#     print(i)

# for i in range(-3, -16, -1):
#     print(i)


# table of 5

# n = int(input("Enter Number: "))
# for i in range(1, 11, 1):
#     print(n*i)




a = "Kanishq"

# len() => also adds spaces in length

# iterate through indexes
# for i in range(len(a)):
#     print(a[i])

# # iterate directly over string
# for char in a: 
#     print(char)


# for i in range(1, 21):
#     if i == 8:
#         continue
#     else:
#         print(i)


# n = int(input("Enter Number: "))
# for i in range(n):
#     print("Hello World")

# for i in range(n, 0, -1):
#     print(i)

# sum = 0
# for i in range(n+1):
#     sum += i

# print(sum)


# fact = 1
# for i in range(1, n+1, 1):
#     fact *= i

# print(fact)


# sumE = 0
# sumO = 0

# for i in range(n+1):
#     if(i % 2 == 0):
#         sumE += i
#     else:
#         sumO += i

# # print("Sum of Even Numbers:",sumE, "Sum of Odd Numbers:", sumO)


# sum = 0
# for i in range(1, n):
#     if(n % i == 0):
#         sum += i



# # print(sum)
# if(sum == n):
#     print(n, 'is a perfect number')
# else:
#     print(n, 'is not a perfect number')



# cnt = 0
# for i in range(1, n):
#     if(n % i == 0):
#         cnt += 1

# if(cnt > 1):
#     print("Not a prime number")
# else:
#     print("Prime Number")



# Reverse a string without using in build functions & Palindrome
# name = "naman"

# temp = ""
# n = len(name)

# for i in range(n):
#     temp = temp + name[n-1-i]


# if(temp == name):
#     print("String is Palindrome")
# else:
#     print("String is not a palindrome")



# 2. While Loop

# a. seperate each digit and print
# n = 101

# while n > 0:
#     print(n % 10)   #printing last digit
#     n = n // 10     #shrinking the number




# b. input a number and reverse it
# n = int(input("Enter a number: "))

# rev = 0

# while(n > 0):
#     rev = rev * 10 + n % 10     
#     n = n // 10

# print(rev)



# c. Accept a number and check if it's a palindromic number
# n = int(input("Enter a number: "))

# temp = n
# rev = 0

# while(n > 0):
#     rev = rev * 10 + n % 10     
#     n = n // 10

# if(temp == rev):
#     print("Palindromic")
# else:
#     print("Not Palindromic")



# d. Create a random number guessing game with python

# import random

# num = random.randint(1, 10)
# i = 3

# while (i > 0):
#     n = int(input("Guess the number: "))
#     if(num != n):
#         print("Wrong, guess again!")
#     else:
#         print("Guessed right!!")

#     i = i - 1






# Functions

# a = 23
# b = 24

# def func(n1, n2 = 34):
#     print("Sum: ", n1 + n2)

# func(a)


# def palindrome(st):
#     rev = ""
#     for i in range(len(st)-1, -1, -1):
#         rev = rev + st[i]
    
#     if(rev == st):
#         print("palindrome")
#     else:
#         print("not a palindrome")


# palindrome("naman")


# def func():
#     return "hello how are you"

# print(func())






# Data Structure -> List, Tuple, Sets, Dictionaries

# 1. List -> mutable, ordered, duplicates, hetrogeneous

# temp = [1, 2, 3, 4, 5, 5]
# print(temp)
# temp[1] = 23
# print(temp) 

# ump = [1, "1", 2, "2"]
# print(ump)

# for i in range(len(temp)):
#     print(temp[i])


# for i in temp:
#     print(i)



# arr = [9, 22, 42, 1, 2, 4]

# largest = arr[0]
# sLargest = 0

# for i in range(1, len(arr)):
#     if(arr[i] > largest):
#         sLargest = largest
#         largest = max(largest, arr[i])
        
#     elif(arr[i] < largest and arr[i] > largest):
#         sLargest = arr[i]


# print(largest, sLargest)



# arr1 = [3, 4, 1, 2]
# arr = [1, 2, 3, 4, 5]

# i = 0

# while i < len(arr) - 1:
#     if (arr[i] < arr[i+1]):
#         i = i + 1
#         continue
#     else:
#         print("Not Sorted")
#         break

# else:
#     print("Sorted")






# 2. Tuple -> Immutable, Duplicates, Ordered, Heterogenous
# temp = (1, 2, 3, 4, 5)
# print(temp)


# ump = (1, 1.2, print(), "hello")

# temp = (1, 2, 3, 4, 4, 5)

# index = temp.index(4)  #index()
# l = temp.count(4)      #count()
# print(index, l)

# a, b, c, d = (1, 2, 3, 4)   #tuple unpacking
# print(b)


# a = (1)  #unpacking occurs that's why type of a is INT
# print(type(a)) 

# a = (1,)  #add (,) so python will understand that it isn't unpacked
# print(type(a))





# 3. Set
# mutable, duplicates -> you cannot have duplicates, unordered -> you cannot access
# them through index values, heterogeneous -> it can store some data types like 
# string, numbers, tuples but not everything

# s1 = {1, 2, 8, 3, 3, 4}
# s2 = {5, 3, 5, 6, 7,8}

# # s1 = s1.union(s2)  # s1 | s2
# # s1 = s1.intersection(s2)  # s1 & s2
# # s1 = s1.difference(s2)  # s1 - s2
# # s1 = s1.symmetric_difference(s2)  # s1^s2
# print(s1)

# for i in st:  # set traversing
#     print(i)

# st.add(99)  # add the value
# st.remove(8)  # remove the shown value
# st.discard(0)  # no error if value not found
# st.pop() # removes first element
# st.clear()  # clear all the elements

# print(st)




# 4. Dictionaries -> Mutable, Duplicates => Keys must be unique but values can hold
# duplicates, order => dictionary follows insertion order, heterogeneous

# d = {1: "Hello", 2: "Kanishq"}
# d[1] = "Hi"  #mutable    # updating

# d[100] = "Hello"   # creating

# del d[1]   # deleting

# d1 = {"hi": 1, "h": "kanishq23"}  # heterogeneous


# print(d)


d = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}

# d1 = d   # deep copy, copied one will not be independent
# d2 = d.copy()  # shallow copy, copied one will be independent 

# # d.clear()  # clear all the elements

# # for i in d:
# #     print(d[i])


# print(d.get(2))    # Get the value by key
# print(d.items())   # shows items of dict
# print(d.pop(3))    # remove the specified key and return the value



# Merge two python dictioanries
# d1 = {1: 100, 2: 200, 3: 300}
# d2 = {3: 400, 4: 400, 5: 500}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
    
#     else: d1[i] = d2[i]

# print(d1)

# for i in d2:
#     d1[i] = d2[i]

# print(d1)



# Sum all the values of dictionary
# sum = 0
# for i in d1: 
#     sum += d1[i]

# print(sum)



# count the frequency of elements
# a = [1, 1, 2, 2, 2, 3,3 , 33, 3, 4]
# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)







# Exception Handling
# Exceptions are the unexpected events that occurs during the execution 
# of a program, which disrupts the normal flow of the program

# a = int(input("Enter Number: "))

# try:
#     print(10/a)
# except Exception as err:    # Generalises all the errors 
#     print("sorry error", err)

# else:     # run when no exception occurs
#     print("no exception occurs")


# finally -> runs no matter what
# raise -> manually throws an exception



# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("sorry error")
# finally:
#     print("Ok i have done the division")






# File Handling
# r -> read only,  w -> Write in the file or Overwrite the whole data
# a -> append

# p = open('one.txt', 'a')

# p.write("Hello this is kanishq and writing inside this file")
# p.write("append material")

# p.close()
