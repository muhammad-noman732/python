def vowels_in_string (string):
    # vowels = "aeiouAEIOU" is use to track of all vowels that exist
    vowels ="aeiouAEIOU"
    # count is varibale to count number of vowels 
    count = 0 
    # for loop to iterate over values
    for val in string:
        # it check the value of string in vowels like if string is noman then at first index 
        # values is n so it check if s== aeiouAEIOU if this condition is true tha it add 1 to count 
        if val in vowels:
            count +=1
    # return count ->total number of vowles
    return count
st= input("enter a string")
res = vowels_in_string(st)
print("vowels in string are " , res)
