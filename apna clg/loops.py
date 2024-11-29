# while loop

# Q1- print numbers from 1 to 100
# i=1
# while i <=100:
#     print(i)
#     i+=1

#  ++++++++++++++   Q2- print numbers from 100 to 1 ++++++++++++++++++
# i = 100
# while i >= 1:
#     print(i)
#     i=i-1

# +++++++++++++++ Q3 print multiplication table of number n +++++++++++++++++
# n= 3
# n = int(input("enter a table number "))
# i = 1
# while i <= 10:
#     print(n ,"x" , i ,"=", n * i)
#     i+=1

# +++++++++++++ print element of list using loop== list=[1,4,9,16,25,36,64,81,100] ++++++++
# idx = 0 
# list = [1,4,9,16,25,36,64,81,100]
# while idx <=len(list)-1:
#      print(list[idx])
#      idx += 1

# search for a number x in the tuple using loop

# tuple = (1,4,9,16,25,36,64,81,100)
# x= int(input("enter a number to search"))
# idx = 0 
# while idx < len(tuple):
#     if (tuple[idx] ==x) :
#         print("element x ", x ,"is found at index",idx)
#         break
#     idx+=1
# else: 
#     print("Element", x, "not found in tuple")
    
# continue . it is like skip when continue will come the next statemnt will be skipped for
# i= 1
# while i <=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# print only even numbers
# i=0 
# while i <=10:
#     if(i%2 != 0 ):
#         i+=1
#         continue
#     print(i)
#     i+=1
# # print only odd numbers
# i=0 
# while i <=10:
#     if(i%2 == 0 ):
#         i+=1
#         continue
#     print(i)
#     i+=1

# +++++++++++++++++++++++ For Loop +++++++++++++++++++++++++++

# Q1-print the element of fllowing list using for loop 
# list = [1,4,9,16,25,36,64,81,100]
# for el in list:
#     print(el)

# Q2-search for a number x in the tuple using for  loop
# tuple = (1,4,9,16,25,36,64,81,100,16)
# x= int(input("enter a number for search"))
# idx = 0 
# for el in tuple:
#     if(el == x):
#         print("element is found at index " , idx)
#         break
#     idx+=1

#  Range()  start by default from 0  and one step increase 
# seq = range(5) 
# print(seq[0])
# print(seq[1])
# print(seq[2])
# for el in seq:
#     print(el)

# print even numbers from 1 to 10
# for i in range(2,11,2):
#     print(i)

# practice question 
# Q1 print numbers from 1 to 100
# for i in range(1,101,1):
#     print(i)

# Q2 print numbers from 100 to 1
# for i in range(100 ,0,-1):
#     print(i)

#  Q3 print the multiplication of table n 
# table = 3
# for n in range(1,11,1):
#     print(table,"x", n ,"=", table *n)

# important question
# WAP to find sum of first n numbers using while loop(using list )
# list=[1,2,3,4,5,6,7,8,9,10]
# i = 0 
# sum = 0 
# while i < len(list):
#     sum = sum + list[i]
#     i= i+1
# print(sum)
    
# WAP to find sum of first n numbers using for loop
# n = 5 
# sum =0 
# for i in range(1, n+1):
#     sum+=i
# print(sum)

# WAP to find the factorial of first n number using for loop 
# n = 6
# fac = 1
# for i in range(n , 0, -1):
#     fac = i*fac
# print(fac)
#5*4*3*2*1

n = 10
a = 0
b = 1
for i in range(n):
    print(a)
    a,b= b , a + b # Update a to the old value of b, and b to the sum of a and b

             
# 0,1,1,2,3,5,8,13,21,35
