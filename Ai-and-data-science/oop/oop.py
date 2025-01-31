class point:
    # constructor in pyhton
    def  __init__(self , x= 0 , y = 0):
        self.x = x 
        self.y = y
    # string representstion of point class or object of it
    #  
    # is method ko chlane k liye bar bar call krna pre ga 
    # def get_human_readable(self):
    #     return "[" + str(self.x) + "," + str(self.y) + "]"

    # so alterntive is built in method jis se object ki string representation automatic ho jaegi
    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"


    
# here p1 is refrence variable it stored the refrence of object it is not pointer but it work same as pointers in cpp

p1 = point() # here p1 is refrence variable
print("p1 :",p1.x)
p2 = point(2,4)
print("p2 :" ,  p2.y)
# rsult = p2.get_human_readable()
# print(rsult)
#  now this print(p2) will give result instead of address because use of __str__
print(p2)
# print(p1) # it wil give address <__main__.point object at 0x0000024948B25B50>  so for getting result in form of string we have to define a method 

    # COMPOSITION
    # ik class k andar kisi aur class ka instance rakhna h
class Shape:
        def __init__(self , point):
            self.point = point
        # fro string representation
        def __str__(self):
            ret = ""

            for i in self.point:
                ret += str(i) + " - "
            return ret

p1 = point(5,5)
p2 = point(10,5)
p3 = point(5,10)
p  = [p1,p2,p3]
sh = Shape(p)
print(sh)
# this is most reason why pyhton is using in data science
# in pyhton we can add method to class after it is defined
# it is different from friends function we can access it through object of class but not friend function
def print_points(self):
    for i in self.point:
         print(i)
Shape.print_points = print_points
sh.print_points()

#----------------------- inheritance ---------------------

class Triangle (Shape):
    pass

t = Triangle(p)
t.print_points()

#  concept of override in inheritance
class Rectngle :
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area( self):
        return self.length * self.width
    def permeter(self):
        return 2* self.length + 2* self.width
    def __str__(self):
        return "L: " + str(self.length) + " , W: " + str(self.width)

reac = Rectngle(2 , 4)
print(reac)
# p = reac.permeter()
# print(p)
class Square(Rectngle):
    def __init__(self , length):
        super().__init__(length, length)
    
    def __str__(self):
        return "square: "+ super().__str__()

square = Square(4)
# print(square)


