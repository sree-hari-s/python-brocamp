class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        n = self.head

        if n == None:
            print("List is empty")
        else:
            while n is not None:
                print(n.data,"-->", end=" ")
                n = n.ref
            print()

    def insert_first(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = Node(data)

        n = self.head

        if  n == None:
            self.head = new_node
            self.tail = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            self.tail = new_node

    def insert_after(self, data, x):
        
        if self.head == None:
            print("Empty linked list")
            return
        
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        
        if n == None:
            print("Element not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


    def insert_before(self, data, x):

        if self.head == None:
            print("Empty linked List")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
            
        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n == None:
            print("Element not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delete_first(self):
        if self.head == None:
            print("Empty list")
            return
        self.head = self.head.ref

    def delete_last(self):
        if self.head == None:
            print("Empty list")
            return
        n = self.head
        while n is not None:
            if n.ref.ref == None:
                break
            n = n.ref
        if n == None:
            print("Node note found")
        else:
            n.ref = None
    
    def delete_node(self, x):
        if self.head == None:
            print("Node not present")
            return

        if self.head.data == x:
            self.head = self.head.ref
            return

        n = self.head

        while n != None:
            if n.ref.data == x:
                break
            n = n.ref
        
        if n == None:
            print("Node not present")
        else:
            n.ref = n.ref.ref
    
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.ref
            current.ref = prev
            prev = current
            current = next
        self.head = prev
    
    def dis_arr(root):
        while (root != None):
            print(root.data, end=" ")
            root = root.ref

    def array_to_list(self):
        arr = [1,23,4,6,89]

        n = len(arr)
        node = None
        for i in range(n - 1, -1, -1):
            new_node = Node(arr[i])
            new_node.ref = node
            node = new_node

        while node is not None:
            print(node.data,"-->",end=" ")
            node = node.ref
    




list = LinkedList()
list.array_to_list()
# list.insert_last(90)
# list.insert_first(10)
# list.insert_last(100)
# list.insert_first(45)
# list.insert_after(33, 10)
# list.insert_last(101)
# list.insert_before(2, 101)
# list.delete_first()
# list.delete_last()
# list.delete_node(2)
# list.display()
# list.reverse()
# list.display()