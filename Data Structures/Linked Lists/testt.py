class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class singly:
    def __init__(self) -> None:
        self.head =None
        
    def traversal(self):
        print()
        if self.head is None:
            print("empty list")
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
            
    def begin(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    def end(self,data):
        ne = Node(data)
        a = self.head
        while a is not None:
            a = a.next
        a.next = ne
    
    def insert(self,position,data):
        nib = Node(data)
        a = a.next
        for i in range(1,position-1):
            a = a.next
        nib.next = a.next
        a.next = nib