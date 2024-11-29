#                           Assignment 01 
#                           part1: conditional questions

#  Q-1- chechk wether the given number is positive , nehative or 0 
number = int(input("enter the number"))
if number > 0:
    print("number is positive")
elif number < 0 :
    print("number is negative")
else:
    print("number is equal to 0 ")

# Q2- Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int (input("enter your age"))
if(age > 18):
    print("they are senior citizen")
elif age ==18:
    print("adult")
else:
    print("minor")

# Q-3-Write a program that checks if a given year is a leap year.

year = int(input("enter the year"))
if year % 4 == 0:
    print("leap year")
else:
    print("no it,s not leap year")

# Q4-Take an integer and check if it’s even or odd.

num = int(input("enter the integer"))
if num %2 == 0:
    print("the number is even :")
else:
    print("the number is odd :")

# Q.5-Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

grade_percentage = int(input("enter the percentage of grade"))
if grade_percentage >= 90:
     grade = 'A'
     print("your grade is : " , grade)
elif grade_percentage >=80:
     grade = 'B'
     print("your grade is : " , grade)
elif grade_percentage >=70:
     grade = 'C'
     print("your grade is : " , grade)
elif grade_percentage >=60:
     grade = 'D'
     print("your grade is : " , grade)
else:
     grade = 'F'
     print("your grade is : " , grade)
    

# Q-6- Write a program to find the largest of two numbers.
num1 = int(input("enter the 1st number : "))
num2 = int(input("enter the 2nd number : "))
if num1 > num2:
     print("num1 is greater than num2 : ")
else:
     print("num2 is greater than num1 : ")

#Q- 7. Write a program to find the largest of three numbers.

num1 = int(input("enter the 1st number : "))
num2 = int(input("enter the 2nd number : "))
num3  = int(input("enter the 3rd number : "))
if num1 > num2  and num1 > num3:
     print("num1 is greater than num2 and num3 : ")
elif num2> num1 and num2 >num3:
     print("num2 is greater than num1 and num3 : ")
else:
     print("num3 is greater than num1 and num2 : ")

# Q8-Create a program that checks if a given string is a palindrome.
str = input("enter a string")
reversed_string = str[ :: -1]
if  str == reversed_string:
    print(reversed_string)
    print("string is palindrom")
else:
    print("string is not palindrom")

      

# q9-Take three sides of a triangle as input and check if they form a valid triangle.

side1 = int(input("enter 1st side of triangel: "))
side2 = int(input("enter 2nd side of triangel: "))
side3 = int(input("enter 3rd side of triangel: "))

if side1 + side2 > side3 and side2 +side3 > side1 and  side1+side3> side2:
    print(" tringle is valid tringle :")
else:
    print(" tringle is not valid tringle :")

# Q.10:Write a program to determine if a given character is a vowel or consonant.

char = input("enter a character :")
if len(char) != 1:
    print("enter a single character  ")
else:
    if char in "AEIOUaeiou":
        print("the character is vowel")
    else:
     print("the character is consonant")
       
# Q11-Check if a given number is a multiple of both 3 and 5.

num = int(input("enter a number :"))
if num %3 == 0 and num%5 == 0:
    print("number is multiple of 3 and 5")
else:
      print(" number is not multiple of 3 and 5")

# Q12-Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

cels_temperatre = int(input("enter temperature in celcius : "))
if cels_temperatre <=0:
    print("its freezing")
elif cels_temperatre > 10 and cels_temperatre <25:
    print("it,s moderate")
else:
    print("its hot")

#Q13-Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = int(input("enter 1st number: ")) 
num2 = int(input("enter 2nd number: ")) 
operator = str(input("enter an operator (+,-,*,/,%: )"))

if  operator == "+":
     print("num1 + num2 = " , num1 + num2)
elif operator == '-':
     print("num1 - num2 =" , num1 - num2)
elif operator =="*":
     print("num1 * num2 = " , num1 * num2)
elif operator =="/":
     print("num1 / num2 =" , num1 / num2)
elif operator =="%":
     print("num1 % num2 =" , num1 % num2)
else:
     print("enter a valid operator")

# Q14-Check if a year input by the user is a century year.

year =  int(input("enter the year: "))
if year %100 == 0:
    print("century year  ")
else:
    print("not century year  ")

# Q15-Write a program to check if a number is within a specified range.

num = int(input("enter the number: ")) 
lower_bound = int(input("enter lower bound: "))  
upper_bound = int(input("enter upper bound: "))
if num < upper_bound and num > lower_bound:
    print(f"number {num} is in the range of [{lower_bound} ,{upper_bound}]")
else:
    print(f"number {num} is in the range of [{lower_bound} ,{upper_bound}]")


# Q16-Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).

side1 = int(input("enter 1st side of triangle: "))
side2 = int(input("enter 2nd side of triangle: "))
side3 = int(input("enter 3rd side of triangle: "))
if side1==side2== side3:
    print("equilateral triangle :")
elif (side1==side2 or side1==side3 or side2==side3 )and(side1!=side3 or side2 !=side3):
    print("isosceles tringle:")
else:
    print("scalene tringle:")

# 17-Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
number = int (input("enter a number :"))
if number %2 == 0 and number%3 !=0:
    print("it’s divisible by  2")
elif number % 3 == 0 and number%2 !=0:
    print("it’s divisible by  3")
else:
        print("it’s divisible by both")

# Q18-Take a user’s score and determine if they pass or fail (pass if 50 or above).
score = int (input("enter your score :"))
if score >=50:
    print("pass")
else:
    print("Fail")

# Q19- Check if a string input is uppercase, lowercase, or a mix.

string = str(input("enter a string :"))
if string.islower():
    print("lowercase")
elif string.isupper():
    print("uppercase")
else:
    print("mix")

# Q20- Create a program that evaluates if an inputted number is prime.
num = int (input("enter your score :"))

