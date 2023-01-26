#doubly linked lists
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def forward_traversal(self):
        print()
        if self.head is None:
            print("Empty linked list")
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
                
    def backward_traversal(self):
        print()
        if self.head is None:
            print("Empty linked list")
        else:
            a = self.head
            while a.next is not None:
                a= a.next
            while a is not None:
                print(a.data, end=" ")
                a = a.prev
                
    def insert_at_beginning(self,data):
        ns=Node(data)
        a = self.head
        a.prev = ns
        ns.next = a
        self.head = ns
        
    def insert_at_end(self,data):
        ne=Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        ne.prev = a
        
    def insert_at_specific_node(self,position,data):
        nib = Node(data)
        a = self.head
        for i in range(1,position-1):
            a = a.next
        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib
    
    def deletion_at_beginning(self):
        a=self.head
        self.head = a.next
        a.next = None
        self.head.prev = None
        
    def deletion_at_end(self):
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None
        a.prev = None
        
    def deletion_at_specific_node(self,position):
        a = self.head.next
        b = self.head
        for a in range(1,position-1):
            a = a.next
            b = b.next
        b.next = a.next
        a.next.prev = b
        a.next = None
        a.prev = None
        

dll = doublyLinkedList()
n1 = Node(5)
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next=n2
n3 = Node(15)
n3.prev = n2
n2.next=n3
n4 = Node(20)
n4.prev = n3
n3.next=n4
dll.forward_traversal()
dll.backward_traversal()
dll.insert_at_beginning(100)
dll.forward_traversal()
dll.insert_at_end(200)
dll.forward_traversal()
dll.backward_traversal()
dll.insert_at_specific_node(3,300)
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_beginning()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_end()
dll.forward_traversal()
dll.backward_traversal()
dll.deletion_at_specific_node(2)
dll.forward_traversal()
dll.backward_traversal()
