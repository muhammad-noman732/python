# string and conditional statement.
name = "noman"
first_char = name[0]
print(first_char)

# slicing 
name = "Muhammad Noman"
print(name[0:7])
print(name[3:]) # ammad Noman
print(name[:]) #  Muhammad Noman
print(name[2:10:2]) # hma 

# Negative slicing
# slicing starts from end
print(name[-5:-1])
# String Functions 
# 1.endswith()
str = "hello coder how are you"
print(str.endswith("he"))  # if it end with this than return True else False
# 2- Capatalize() . to captalize first character
print(str.capitalize())
# 3-replace() to replace some value in string 
print(str.replace("coder","programmer"))
# 4 - find()- it will return first index of word that we want to find
print(str.find("are"))
# 5- count() - to count occurence of a letter or word
print(str.count("o"))

# PRACTICE QUESTIONS 
# Q-1 WAP to input user,s first name and writes its length
username= (input("enter your first name "))
print("length of your name is" ,len(username))

# Q-2 -WAP to print number of occurence of $ in a string
string = "i have earned 20$ and 1$ prize is 273 rupees"
print("the occurence of $ is " , string.count("$"))

# CONDITIONAL STATEMENT 
marks= int(input("enter the marks of students"))
if(marks >=90 ):
   grade ="A"
elif( 90 > marks and marks >= 80):
     grade ="B"
elif(80 > marks and marks >=70):
     grade ="C"
elif(70 > marks ):
      grade ="D"
print("grades of students is " , grade)

# NESTING -if ke andar ik aur if 
age = 98
if( age > 18):
    if(age > 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can not drive") 

#  PRACTICE QUESTIONS::
# Q-1- WAP chechk number entered by user is odd or even 
num = int(input("enter a number "))
if(num %2 ==0):
    print("number is even")
else:
   print("numbe is odd")

# Q-2 - WAP  to find the greatest of three number entered by user
num1 = int(input("enter 1st number "))
num2 = int(input("enter 2nd number "))
num3 = int(input("enter 3rd number "))
if(num1 > num2 and num1 > num3):
    print("num1", num1 ,"is greatest")
elif(num2 > num1 and num2 > num3):
     print("num2", num2 ,"is greatest")
else:
    print("num3 ", num3 ,"is greatest")

# Q3 -WAP to program to check if number is multiple of 7 or not
num = int(input("enter a number"))
if(num % 7== 0 ):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")