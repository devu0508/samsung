class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NONE")

def merge_lists(list1, list2):
    current1 = list1.head
    while current1:
        current2 = list2.head
        prev2 = None
        while current2:
            if current1.data == current2.data:
                if prev2:
                    prev2.next = current2.next
                else:
                    list2.head = current2.next
                current2.next = current1.next
                current1.next = list2.head
                return
            prev2 = current2
            current2 = current2.next
        current1 = current1.next
        
def get_linked_list():
    linked_list = LinkedList()
    elements = input("Enter the elements of the linked list separated by spaces: ").split()
    for elem in elements:
        linked_list.append(int(elem))
    return linked_list

print("Enter elements of the first list:")
l1 = get_linked_list()

print("Enter elements of the second list:")
l2 = get_linked_list()

print("Original list 1:")
l1.print_list()

print("Original list 2:")
l2.print_list()

merge_lists(l1, l2)

print("Merged list:")
l1.print_list()
