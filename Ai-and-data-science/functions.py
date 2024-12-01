#              function and recursion
# solving  question of function and recursion to improve logic building 

                    # Basic Function Questions

#Q1. Write a function to calculate the area of a circle given its radius.
 
# def area(rad):
#     # return 6.28 * rad
#     radius = 3.14 * rad * rad
#     print("area of circle is " ,   radius )

# radius = int(input("enter your radius:"))
# area(radius)
# # Area = area(radius)
# # print("area of circle is :" , Area)

#Q2. Create a function that takes two numbers and returns their sum.

# def sum(a , b):
#     return a+b 

# num1 = int(input("enter 1st num:"))
# num2 = int(input("enter 2nd num:"))
# ans = sum(num1 , num2)
# print("sum of two numbers :", ans)

# 3. Write a function to find the factorial of a number using recursion.

# def factorial(num):
#     # base case 
#     if num == 0 :
#         return 1
#     return num * factorial(num-1)
    

# num = int(input("enter  number :"))
# fac = factorial(num)
# print(fac)

# 4. Write a function that takes a string and returns it reversed.
# def reversed_string(st):
#     return st[:: -1]
   
# string= input("enter a string ")
# st =reversed_string(string)
# print("reversed string is :" , st)

#      another method 
# As we cannot direclty change string as it is immutable so 
# 1 - convert to list
# use to pointer and reverse
# Again use join to convert list to string
 
# def reversed_string(st):
#     string = list(st)
#     start = 0
#     end = len(string) -1 
#     while start <= end:
#         string[start] , string[end] = string[end], string[start]
#         start+=1 
#         end -=1
#     s= "".join(string)
#     return s
   
# string= input("enter a string ")
# st =reversed_string(string)
# print("reversed string is :" , st)

# 5. Create a function to check if a given number is prime.

# def check_prime(num):
#     is_prime= True
#     if num <= 1 :
#         is_prime= False
#     else:
#         for i in range(2 , num):
#             if num % i == 0 :
#                 is_prime = False
#                 break
#     if is_prime:
#         print("number is prime ")
#     else:
#         print("number is not prime ")

# num = int (input("enter a  number :"))
# check_prime(num)

# 6. Write a function to count the vowels in a given string.

# def vowels_in_string(st):
#     count = 0 
#     for i in st:
#          if i in "aeiouAEIOU":
#              count +=1 
#     print(count) 

# string = input("enter a string :")
# vowels_in_string (string)


                            # Intermediate Function Questions

#Q1. Create a function that takes a list of numbers and returns the largest number.

# def maximum_number(nums):
#     for i in nums:
#         return max(nums)
#     # maxi = nums[0]
#     # for num in nums:
#     #     if num >  maxi:
#     #         maxi = num
#     #     return maxi
    
# num = [1,2,3,4,54,32,65]
# max =maximum_number(num)
# print(max)

#Q2. Write a function to find the nth Fibonacci number using recursion.

# def fabinoci_series(n):
#     #  base case
#     if n == 0  or n == 1 :
#         return 1
     
#     return fabinoci_series(n -1 ) + fabinoci_series(n-2)

# # fabinoci-- 0 1 1 2 3 5 8 13 21 ....
# number = int(input("enter a number to ehich find the fbinoci series:"))
# fab = fabinoci_series(number)
# print(fab)

# Q3. Write a function to check whether a string is a palindrome

# def palindrom (st):
#     if st == st[::-1]:
#         print("string is palindrom")
#     else:
#         print("string is not palindrom")

# string =(input("enter a string :"))
# palindrom(string)

#Q4. Create a function that takes a list of integers and returns the sum of all even numbers.

# def evenSum (nums):
#     sum= 0
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0:
#             sum += nums[i]
#     return sum

# arr =[12,21,34,43,2]
# # arr = list(input("enter list of integers"))
# sum = evenSum(arr)
# print("sum of all even numbers is  :" , sum)

#Q5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

# def GCD(a , b):
#     while b!= 0 :
#         a , b = b , a % b
#     return abs(a)
# num1 = int(input("enter 1st number:"))
# num2 = int(input("enter 2nd number:"))
# result = GCD(num1 , num2)
# print("GCD (Greatest Common Divisor) of two numbers.", result )

#Q6. Create a function that accepts a dictionary and returns the key with the highest value.





