class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(pos - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_from_pos(self, pos):
        if self.head is None:
            raise IndexError("Position out of range")
        if pos == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(pos - 1):
            if current is None or current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.add_at_pos(10, 0)  
ll.add_at_pos(20, 1)  
ll.add_at_pos(30, 2)
ll.display()  
ll.delete_from_pos(1)  
ll.display() 
ll.traverse() 
