class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_front(self, data):

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, data):

        if prev_node is None:
            print("previous node cannot be null")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def insert_end(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

        new_node.prev = temp

        return


    def display_list(self, node):

        while node:
            print(node.data, end="->")
            last = node
            node = node.next

d_linked_list = DoublyLinkedList()

d_linked_list.insert_end(5)
d_linked_list.insert_front(1)
d_linked_list.insert_front(6)
d_linked_list.insert_end(9)

d_linked_list.display_list(d_linked_list.head)
