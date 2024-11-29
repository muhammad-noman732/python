#  practice questions
# Q.1- counting positive numbers
# given a list of numbers count how many are positive 
numbers = [1,-2,3,-4,5,6,-7,-3,1,-33]
i=1
positive_number_count=0
for i in numbers:
    if i > 0:
       positive_number_count+=1
print("count is " ,positive_number_count)

# Q2 calculate the sum if even numbers given upto n
n = 10
sum = 0 
for i in range(1 , n+1):
    if i % 2 == 0:
        sum += i
print("sum of even numbers is " , sum)

# Q3-  print the multiplication table upto 10 but skip fifth iteration.
# table_num = int(input("enter the number of table"))
for i in range (1 , 11):
    if i == 5:
        continue
    # print(table_num ,"x", i ,"=" ,table_num * i)

# Q4-  reverse a string
# name="noman"
# reversed_string =""
# for char in range(len(name)-1, -1 ,-1):
#     reversed_string += name[char]
# print(reversed_string)

# Q.5 given a string find a first non- repeating chracter
# word= "teeterajdcweu"
# for char in word:
#     print(char)
#     if word.count(char) == 1:
#         print("the first non repeating char is" , char)
#         break
    
# Q6 calculate factorial of a number using while loop
# fac = 1
# number =5
# i= number
# while i >= 1:
#     fac = fac * i
#     i = i - 1
# print(fac)

# Q_7  validate input 
# kepp asking user for input until they enter the number between 1 and 10

# while True:
#     num = int(input("Enter a number between 1 and 10: "))
#     if 1 <= num <= 10:
#         print("Thanks!")
#         break  # optional: add this to exit the loop once a valid number is entered
#     else:
#         print("Invalid number")

# Q8- prime number
# chechk wether the number is prime or not
# num = 29
# is_prime = True
# if num > 1:
#     for i in range(2 , num):
#         if num % i == 0:
#            is_prime= False
#            break
# print(is_prime)

# Q9- check if elements in the list are unique. if duplicate is found exit the loop and print the 
# duplicate loop
items = ["banana" ,"apple" ,"coconut","apple"]
unique_item = set()
for item in items:
    if item in unique_item:
        print("duplicate :" , item)
        break
    unique_item.add(item)
else:
    print("all the elemets are unique")
   
#

