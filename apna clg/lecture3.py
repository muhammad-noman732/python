# list in pyhton
list =[12,34, 45,32,"noman" , 3.2]
print(list)
# list is mutable 
list[0] = "baghoor"
print(list)

# slicing is same like strings 
print(list[1:]) # [34, 45, 32, 'noman', 3.2]

# methods on list
# append() add a new element at the end of list
list.append(67)
print(list)
#  sort() to sort the list in asending order
item=["noamn" , "baghoor" ,"arsklan"]
item.sort()
print(item)

# the string methods return new string while list methods chnages in original string
item1 = [12,23,10]
print(item1.append(34)) #none bcz this will append not return new 
print(item1.sort()) #none bcz this will append not return new 
print(item1) #[10, 12, 23, 34]

# we can also sort the string in reverse order
item1.sort(reverse = True)
print(item1)

# reverse() . to reverse the string 
list=[90,12,23,34]
list.reverse()
print(list)

# insert() - to insert the value at specific index
list.insert(1,1000)
print(list)

# remove() - to remove the first occurence of element
list1=[12,22,34,22]
list1.remove(22)
print(list1)

# pop() - to remove element from index 
list1.pop(2)
print(list1)

# tuples.
#  tuples are same like list but these are immutable

tuple = (22,"noman" ,True ,3.4 ,21,3.4, 3.4)
print(tuple)
tup=(1,) # if there is one vlue in tuple then it is necessary to use (,) at end otherwise type will be change from tuple to that data 
print(type(tup))  # <class 'tuple'>
print(tup)

# slicing is same like string and lists 

# index() return the index of first occurence 
print(tuple.index(3.4)) 

# count() to count the occurence of element
print(tuple.count(3.4))

# PRACTICE QUESTIONS

# q1 WAP ask user to enter three favourite movie and store them in a list 
# movies = []
# movies.append(str(input("enter your 1st movie  ")))
# movies.append(str(input("enter your second movie  ")))
# movies.append(str(input("enter your third  movie  "  )))
# print(movies)

# wap to chechk palidrom or not 
list1 = [1,2,1]
copy_list1 = list1.copy()
list1.reverse()

if(list1 == copy_list1):
    print("list1 is plindrom")
else:
    print("not palindrom")
