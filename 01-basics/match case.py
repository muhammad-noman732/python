x = int(input("enter a number"))


match x:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("another number")
li=[1,2,3,4,5,6,7,8,9]


for x in li:
    print(x)
fac = 5 
num = 1
for i in range( fac ,1 , -1):
    num=num*i
    print(num)
