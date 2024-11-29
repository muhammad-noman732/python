# data ka type hmesha memory k andar objects m hota h variable m nhi hota
# python m data types nhi hoti pr memory k andar jo bhi h uska data types hota h
a=3
a="chaiaurcode"
a=3.14
print(a)
# important 
a=5
b=2
a=a+2
print(a)

#inner working
#a = 5          # `a` points to the integer `5`, which is immutable
#a = a + 2      # A new integer `7` is created, and `a` points to it (no modification of `5`)
#print(a)       # Output: 7

# 
myListOne=[1,2,3,4]
myListTwo=myListOne # here copying the refrence not actual content
myListOne="hello , smit"
print(myListTwo)
# jb list ko ik hi refrence de
l1=[1,2,3]
l2=l1
print(l1)
print(l2)
l1[0]=44
print(l1)
print(l2)
#jb list m refrence change kre 
p1=[1,2,4]
p2=p1
p2=[1,2,4]
p1[0]=44
print(p1)# [44, 2, 4] // ab yha pr p2 ka refrrence change ho gya to usme same value nhi ho gi
#q k list mutable h
print(p2) #[1, 2, 4]

#copy 
h1=[1,2,3]
h2=h1[:] # ye copy create kre ga like slice .. This creates a shallow copy of `h1`
h1[0]=[32]
print(h1) # [[32], 2, 3]
print(h2) #[1, 2, 3]

# most important 
# == checks if two variables have the same value.
# tis checks if two variables refer to the same object in memory (i.e., it checks the reference).

n =[1,2,3]
m = n
print(m)
print(n)
m==n #true
n is m # it is true but it checks refrence of objects not values
n=[1,2,3]
n==m # True ,, bzc values are same 
# but here it differs
n is m # false because of change in refrences


