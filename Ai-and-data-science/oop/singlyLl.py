class Node:
    def __init__(self , data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

# operation of linked list .
# push()

    def push(self , val ):
       # first create a new node that we can use 
        new_node = Node(val)
    # case 1 , when list is empty there is no node
        if self.head is None:
           print("case 1")
           self.head  = new_node
           return
    # case 2 : where there is at least one node
        print("case 2")
        last = self.head
        while last.next is not None:
            last = last.next 
        last.next = new_node
# # now we can add function to class as we can do in python
# LinkedList.push = push

# 2- pop() operation
    def pop(self):
        # agra koi bhi not nhi h to 
        if self.head is None:
            return "list is empty:"
        # two cases 
        # cas1 . when only one node 
        print("case 1")
        if self.head.next is None:
            val = self.head.data
            # pyhon m garbage value ko khtm krna hota delte ka use nhi krna hota interperator automatically memory free  kr deta h 
            self.head = None
            return val
        # when there is at least two node mean more than one 
        print("case 2")
        temp = self.head
        while temp.next is not None:
            previous = temp
            temp = temp.next
        res = temp.data
        previous.next = None
        return res

# method for insertion of node at beginnings 
    def inser_at_beginning(self , val):
        new_node = Node(val)
        # case 1 , when there is no node , list is empty 
        if self.head is None:
            self.head = new_node
            return
        # case 2 , when there is at least one node
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
            return
        
    # method for insertion of node at position

    def insert_at_any_position(self , val , index):
        new_node = Node(val)
        # agar position start m h 
        if index == 0 :
            new_node.next = self.head
            self.head = new_node
            return
        # for any other poistion
        temp = self.head
        counter = 0 
        previous = None
        while temp is not None and counter < index:
            previous = temp 
            temp = temp.next
            counter += 1
        # yha se agar node 3 h aur position last di jati h 3 to wha pr bhi kre insert kregawhen ract 
        # 1->2->3  and position is 3 then
        # when counter is 3 but temp is null in this case previous ke next m new node aye ga aur new node ka next null hoga 
        previous.next  = new_node   
        new_node.next  = temp
        
    def __str__(self):
        ret_str = "["
        temp = self.head

        while temp is not None :
            ret_str += str(temp.data) + ", "
            temp = temp.next
    
        ret_str = ret_str.rstrip(", ")  # Remove trailing comma and space
        ret_str += "]"
        return ret_str 

l1 = LinkedList()
l1.push(3)
l1.push(34)
l1.push(31)
# l1.push(21)
l1.inser_at_beginning(9)
l1.insert_at_any_position(4,3)
# print("pop" , l1.pop())
# print("pop" , l1.pop())
# print("pop" , l1.pop())
# print("pop" , l1.pop())
# print("pop" , l1.pop())
print(l1)
        


        

