
import time
            #   part2 loops
# Q1-Print numbers from 1 to 20 using a for loop.
for i in range( 1, 21):
    print(i)

# Q2-. Use a while loop to print even numbers from 1 to 50.
i = 1
while i <= 50 :
    print(i)
    i+=1

# Q3- Write a program to calculate the sum of all numbers between 1 and 100.
sum = 0 
for i in range (1 , 101):
    sum += i
print( "sum =", sum )

# Q-4. Print the multiplication table of a given number.
table = int(input("enter a table number :"))
for i in range (1, 11):
    print(table , "X" , i ," = " , table *i)

# Q5-Print all odd numbers between 1 and 100 using a loop.
for i in range(1, 101):
    if i %2 !=0:
        print(i)

# Q-6- Use a for loop to print each character of a string.
str= "noman"
for i in str:
    print(i)


# Q-7 Find the factorial of a number using a while loop.
fac = 1 
number = int(input("enter a number :"))
if number == 0:
    print("factorial of 0 is 1 ")
elif number < 0:
    print("factorial is not defined for negative numbers")
else: 
     while number > 1:
        fac = fac * number
        number = number-1
        print("factorial is :" , fac)
# # 5*4*3*2*1

# Q8-Use a for loop to print numbers from 10 down to 1.
for i in range (10 , 0 , -1):
    print(i)

# Q-9. Write a program to print the first 10 Fibonacci numbers.
a = 0
b = 1
for i in range (1 , 11):
     print(a)
     a , b = b , a+b 
# a= 1 ,b= 1 
# 0,1,1,2,3,5,8,13,21,34
# 0 , 0+1 , 1+1 ,

# Q10.Use a loop to count the number of digits in an integer.
count = 0
num = int(input('enter a  number :'))
if num == 0:
        count = 1 
else:
        while num  > 0:
            num = num // 10
            count += 1
            
         
# print(count)

#Q11-  Print the reverse of a given number.
num = int(input('enter a  number :'))
reversed_num = 0 
while num > 0 :
#     first find remainder to get last digit 
      last_digit = num % 10 # if num is 123 then 123 % 10 = 3
#       store last digit in reversed_num so 
      reversed_num  = reversed_num * 10 + last_digit # multiply by 10 bcz first we have 3 remainder than again 2 when multiply 3 by 10 get 30 +2 which give 32 then it will shift 3 one position left
      num = num //10 # this will remove last digit
print("reversed number is " , reversed_num)      


# Q12-Print all prime numbers between 1 and 50.

for num in range(1, 51):  # Loop through numbers from 1 to 50
    is_prime = True  # Reset is_prime for each new number

    if num <= 1:
        is_prime = False  # 1 and below are not prime
    else:
        for i in range(2 , num , 1):  
            if num % i == 0:
                is_prime = False
                break  # No need to keep checking if a divisor is found

    if is_prime:
        print(num)  # Print the number if it is prime
##  primeNumber = 2 , 3 ,5 , 7,11,13, 17 ,21 , 29,37,41,47


# Q13-Use nested loops to print a pyramid pattern of *.

rows = 5
for i in range( 1 , rows+1 ):    #to onclude last row
        # Print spaces
    for j in range(rows - i):
         print(" ", end="")
          
    for k in range( 2 *i-1 ):
       print("*", end="")
    print()

# Q14- write a program that break the loop when certain condition is met:

num = int(input("enter a number :"))
for i in range(1 , num+1):
   if i == 7:
      break
   else:
      print(i)

       
# Q15-print the sum of even and odd numbers separately upto given numbers
num = int(input("enter a number :"))
even_sum = 0
odd_sum  = 0
for i in range(1 , num + 1):
   if i % 2== 0 :
      even_sum += i
   else:
     odd_sum += i
print("odd sum is = " , odd_sum)
print("even sum is =" , even_sum)


# Q16 - write a program to find sum of number of inputted integer
integer = int(input("enter a positive integer :"))
integer_sum = 0 
if integer <=0 :
   integer_sum = 0 
else:
   while integer > 0 :
      #  find last digit 
      last_digit = integer % 10 # 123 % 10 = 3
      integer_sum += last_digit # 0+ 3 ->3+2 ->5+1 =6
      # remove last digit 
      integer = integer // 10 
print("sum of positive integer is :" , integer_sum)
# 123 =1+2+3

# Q19 -use for loop to print sqaure of each number using 1 to 10.
for i in range( 1 , 11):
    print ( "square of " , i, "is", i * i  ) 
  
#  Q20- write a programt that simulate a countdown timer starting from given number down to 0
start = int(input("enter a number :"))
while start > 0 :
   print(start)
   time.sleep(1)     # Pause for 1 second time.sleep(1)
   start-=1
print("count down end ")
