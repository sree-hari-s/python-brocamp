#CREATING A NODE    
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("Empty linked list")
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    
    def insert_at_beginning(self,data):
        print()
        nb = Node(data)
        nb.next = self.head
        self.head = nb
        
    def insert_at_end(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        
    def insert_at_specific_node(self,position,data):
        print()
        nib=Node(data)
        a = self.head
        for i in range(1,position-1):
            a=a.next
        nib.next = a.next
        a.next = nib
        
    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head = a.next
        a.next = None
        
    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        
    def deletion_at_specific_node(self,position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1, position-1):
            a=a.next
            prev=prev.next
        prev.next = a.next
        a.next = None
        
sll = SinglyLL()
n1 = Node(5)
sll.head = n1
n2 = Node(10)
n1.next=n2
n3 = Node(15)
n2.next=n3
n4 = Node(20)
n3.next=n4
sll.traversal()
sll.insert_at_beginning(200)
sll.traversal()
sll.insert_at_end(999)
sll.traversal()
sll.insert_at_specific_node(3,998)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.deletion_at_specific_node(3)
sll.traversal()