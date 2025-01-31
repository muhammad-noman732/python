

#              function and recursion
# solving  question of function and recursion to improve logic building 

                    # Basic Function Questions

#Q1. Write a function to calculate the area of a circle given its radius.
 
def area(rad):
    # return 6.28 * rad
    radius = 3.14 * rad * rad
    print("area of circle is " ,   radius )

radius = int(input("enter your radius:"))
area(radius)
Area = area(radius)
print("area of circle is :" , Area)

#Q2. Create a function that takes two numbers and returns their sum.

def sum(a , b):
    return a+b 

num1 = int(input("enter 1st num:"))
num2 = int(input("enter 2nd num:"))
ans = sum(num1 , num2)
print("sum of two numbers :", ans)

# 3. Write a function to find the factorial of a number using recursion.

def factorial(num):
    # base case 
    if num == 0 :
        return 1
    return num * factorial(num-1)
    

num = int(input("enter  number :"))
fac = factorial(num)
print(fac)

# 4. Write a function that takes a string and returns it reversed.

def reversed_string(st):
    return st[:: -1]
   
string= input("enter a string ")
st =reversed_string(string)
print("reversed string is :" , st)

#      another method 
# As we cannot direclty change string as it is immutable so 
# 1 - convert to list
# use to pointer and reverse
# Again use join to convert list to string

def reversed_string(st):
    string = list(st)
    start = 0
    end = len(string) -1 
    while start <= end:
        string[start] , string[end] = string[end], string[start]
        start+=1 
        end -=1
    s= "".join(string)
    return s
   
string= input("enter a string ")
st =reversed_string(string)
print("reversed string is :" , st)

# 5. Create a function to check if a given number is prime.

def check_prime(num):
    is_prime= True
    if num <= 1 :
        is_prime= False
    else:
        for i in range(2 , num):
            if num % i == 0 :
                is_prime = False
                break
    if is_prime:
        print("number is prime ")
    else:
        print("number is not prime ")

num = int (input("enter a  number :"))
check_prime(num)

# 6. Write a function to count the vowels in a given string.

def vowels_in_string(st):
    count = 0 
    for i in st:
         if i in "aeiouAEIOU":
             count +=1 
    print(count) 

string = input("enter a string :")
vowels_in_string (string)


                            # Intermediate Function Questions

#Q1. Create a function that takes a list of numbers and returns the largest number.

def maximum_number(nums):
    for i in nums:
        return max(nums)
    # maxi = nums[0]
    # for num in nums:
    #     if num >  maxi:
    #         maxi = num
    #     return maxi
    
num = [1,2,3,4,54,32,65]
max =maximum_number(num)
print(max)

#Q2. Write a function to find the nth Fibonacci number using recursion.

def fabinoci_series(n):
    #  base case
    if n == 0  or n == 1 :
        return 1
     
    return fabinoci_series(n - 1 ) + fabinoci_series(n-2)

# fabinoci-- 0 1 1 2 3 5 8 13 21 ....
number = int(input("enter a number to ehich find the fbinoci series:"))
fab = fabinoci_series(number)
print(fab)

# Q3. Write a function to check whether a string is a palindrome

def palindrom (st):
    if st == st[::-1]:
        print("string is palindrom")
    else:
        print("string is not palindrom")

string =(input("enter a string :"))
palindrom(string)

#Q4. Create a function that takes a list of integers and returns the sum of all even numbers.

def evenSum (nums):
    sum= 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum

arr =[12,21,34,43,2]
# arr = list(input("enter list of integers"))
sum = evenSum(arr)
print("sum of all even numbers is  :" , sum)

#Q5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

def GCD(a , b):
    while b!= 0 :
        a , b = b , a % b
    return abs(a)
num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
result = GCD(num1 , num2)
print("GCD (Greatest Common Divisor) of two numbers.", result )

#Q6. Create a function that accepts a dictionary and returns the key with the highest value.

def maxKeyVal (dist):
    highest_val  = float('-inf') # Smallest possible number as the initial value
    highest_key = None
    for key , val in dist.items():
        if val > highest_val:
            highest_val = val
            highest_key = key
    return highest_key
         
my_dict  = {
    "semester":5,
    "age": 33,
    "class":14
}

result =maxKeyVal(my_dict )
print(result)


#                Advanced Function Questions

# Q1. Write a function that calculates the power of a number without using the ** operator.

def power_of_num(num , expo):
    result = 1
    for i in range(expo):
        result *= num
    return result
num = int(input("enter a number"))
exp = int(input("exponential for power"))
res = power_of_num(num ,exp)
print("power of number is" , res)

# 2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

def temp_conversion(tmp , unit):
    if unit == "C":
        # Convert  Celsius to Fahrenheit
        return  (9/5) * tmp +32
    elif unit == "F":
        # Convert Fahrenheit to Celsius
        return  (tmp - 32) * 5/9
    else:
       return "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."

temp  =  float(input("enter temperature " ))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
result = temp_conversion(temp  , unit)
print(result)


#Q3. Write a function to flatten a nested list.

def flatten_list(lst):
    flattened = []
    for element in lst:
        if  isinstance( element, list ):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    return flattened
            
lst= [[1,2],[3,4],[5,6],[7,8],9]
ans = flatten_list(lst)
print(ans)

# Q4. Create a function to check if two strings are anagrams.

def anagram ( s1 , s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if len(s1) != len(s2):
        return False
    for i in range(len (s1)):
        if s1[i] != s2[i]:
            return False
    
    return True
    
s1 = input("enter first string :   ")
s2 = input("enter secoond string : ")
res = anagram(s1 , s2)
print(res)


#Q5. Write a function that takes a list and removes all duplicate elements.

def remove_duplicate_item(li):
    l = 0 
    r = 1 
    while r < len(li):
        if li[l] == li[r]:
            li.pop(r)
        else:
            l += 1 
            r += 1
    return li 

list_item = [0,0,1,1,1,2,2,3,3,4]
result = remove_duplicate_item(list_item)
print("list after removing dupliacte is " , result)

#Q6. Create a function that takes a string and counts the frequency of each character.

def frequency_counter(s):
    # Initialize an empty dictionary to store character frequencies
    dict = {}
    count = 0 
    for i in s:
        if i in dict:
            dict[i]+= 1 
        else:
             dict[i] = 1
    return dict

s = input("enter a string ")
result = frequency_counter(s)
print(result)
 

                    #    Real-world Scenarios

#Q1. Write a function that takes a list of employee salaries and calculates the average salary.

def avg_salary(salary):
    sum  = 0
    avg = 0
    for i in salary:
        sum += i
    avg = sum /len(salary)
    print("average salary of employee is :", avg)
    
salries = [120000,100000,50000,90000, 40000]
avg_salary(salries)


#Q2. Create a function to generate a random password of given length, containing uppercase, lowercase, numbers, and special characters.

import random
import string
def random_password_generate(length):

    if length < 4 :
        return "password length  must be atleast 4 "
    # Define character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure at least one character from each pool
    # selects one characters from one
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
        ]
    
    # Fill the remaining length with random characters from all pools
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    # Shuffle the password and return as a string
    random.shuffle(password)
    return ''.join(password)
 
# Input length and generate the password
length = int(input("Enter the desired password length: "))
print(f"Generated password: {random_password_generate(length)}")
  