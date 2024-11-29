# print("name")
# a= 3 
# b= 4
# sum = a+b
# print(sum)

# operators
# data types
# type casting (implicit and explicit)
# input from user

# Q.1 input to numbers from user and print sum
num1 = int(input("enter your 1st number"))
num2= int(input("enter your 2nd number"))
sum = num1+num2
print(type(num1))
print(sum)

# Q.2 write a program to take input side of square and print its area 
sides = float(input("enter  side of square"))
area = sides * sides
print("Area of square is =", area)

#Q.3 WAP imput two floating numbers and print their average 

number1 = float(input("entet first  number"))
number2 = float(input("entet second  number"))
avg = (number1 + number2 )/2.0
print(avg)

# Q.4 WAP that input two numbers a , b 
# print True if a is greater than or equal. if not  print False

a = int(input("first number "))
b = int(input("second number "))
print(a >= b)