# dectionaries
# these are in key value pairs
# these are unordered , mutable(changable) and canot have duplicae key
# key is immutable so we can,t use dic and lists as a key bcz these are mutable
info = {
    "key" :"value",
    "name":"noman",
    "subjects":["dsa","oop","coal","nc"],
    "topics":("dic" ,"sets"),
    "age":34,
    "cgpa":3.7,
    4.2:3.8,
    (2.21,3) :23,
}

info["name"] = "baghoor"
info["surname"] = "arslan" # this is mutable so we can change the dict
print(type(info))
print(info)
print(info["name"])
print(info["age"])
print(info["cgpa"])
print(info["surname"])

# Null dectionaries
# we can create null dictionaries and use them 
null_dict= {}
null_dict["name"]="python"
print(null_dict)

# nested dectionaries
nested_dict = {
    "class":12,
    "subjetc":{
        "phy" : 85,
        "chem":80,
        "math":99
    }
}
print(nested_dict["subjetc"])
# can also print the marks of any subjects
print(nested_dict["subjetc"]["chem"]) #chem
print(nested_dict)

# methods: 
# keys() . to returns the keys
student = {
    "class":12,
    "subjetc":{
        "phy":85,
        "chem":80,
        "math":99
    }
}
print(student.keys())
print(list(student.keys())) # type cast to list 
print(len(student)) # len of dictionary

# values() to return all the values
print(student.values()) # dict_values([12, {'phy': 85, 'chem': 80, 'math': 99}])
print(list(student.values())) #[12, {'phy': 85, 'chem': 80, 'math': 99}]

# items() to return key values pairs in form of tuples
print(student.items())
print(list(student.items()))
# we can also access individual tuples
pair = list(student.items()) # convert to list than access its index 
print(pair[0])

# get() to get values of keys 
#  we can also get keys by 
print(student["class"]) 
# print(student["class1"])# error
# but in this case if we give wrong key than it will throw error and effect
# the code so we should use get method bcz in this case if key is not present it will give None
print(student.get("class")) 
print(student.get("class")) # None (not error)

# update() to add a new key value pair
student.update({
    "name":"noman",
    "age":20,
    "class":11
})
print(student)


# ++++++++++++++++++++                   sets         +++++++++++++++++++++++++++++++++

# sets have unique value . mutable  and dont have indexing 
# imp. sets are mutable inke andar element add ya remove kia ja skta h but there elements are imutable that can not chnage
collection = { 1,2,3,3,4 ,"hello" , 4.0,"world",3} # duplicate values will be ignored 
print(type(collection))
print(collection)
print(len(collection))

# Empty sets  
collections= set()
print(type(collection))

# Methods on set
# add() to add a new element in set 
# here we can not pass set and dictionary because these element are mutable and sets elements are immutable
collections.add(67)
collections.add(7)
collections.add(67)
collections.add("noman")
collections.add(9.7)
collections.add((1,2,3,4))
print(collections)

# remove() . to remove value if value is not present then it will give error
collections.remove(7)
print(collections)

# clear() . to clear al the values
print(len(collections)) # 4
collections.clear()
print(len(collections)) # 0

# pop() - to remove random value from sets 
set= {12,23,"noman" ,"euvr" ,9.9}
print(set.pop())
print(set.pop())

# set.union(set2) it combine two sets and return a new sets . ignore dupliacte values
set1= {1,2,3,4}
set2={1,3,4}
print(set1.union(set2)) # this will create a new set the originl set will remain same 
print(set1)
print(set2)

# set.intersection(set2) .. combine common values and return new
set1= {1,2,3,4}
set2={1,3,4}
print(set1.intersection(set2)) # this will create a new set the originl set will remain same 
print(set1)
print(set2)

# PRACTICE QUESTIONS 
# q.1 WAP to store word meaning in dectionary
# table: a peace of furniture , "list of facts and figure"
# ctas: "a small animal"

dist = {
    "table":("a peace of furniture" , "list of facts and figure"),
    "cats":"a small animal"
}
print(dist)

# Q.2 - you are given a list of subjects.assume one clssrom is reuired for one subjects. how many classromm 
# are nedded for all subjects 

# we can solve this use sets bcz if use list than it will not ignore duplicate values we need only one room
# for one subject and subject can repeat so use of sets will be good 
subjects= {"python" ,"java","C++" ,"python","javascript","python" ,"java","c","C++"}
print(subjects)
print(len(subjects))

# q-3 WAP ask user to enter marks of 3 subjects and store them in a dictionary.start with empty dictionary and add
# one by one. use subject name as key and marks as values.
marks={}
phy = int(input("enter phy:"))
marks.update( {"phy":phy })
math = int(input("enter math:"))
marks.update( {"math":math })
chem = int(input("enter chem:"))
marks.update( {"chem":chem })
print(marks)



